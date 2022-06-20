import os
import logging
import sqlite3
import urllib.request
import pandas as pd
import numpy as np
from . import cleaning_engineering_functions as cef

class DataProcessing:
    def __init__(self) -> None:

        self.logger = logging.getLogger(__name__) #track the package

        url = "https://techassessment.blob.core.windows.net/aiap11-assessment-data/noshow.db"
        name = "noshow.db"

        if os.path.isfile(name):
            os.remove(name) #if already exist delete it

        urllib.request.urlretrieve(url, name)  # download the file

        cnx = sqlite3.connect(name)
        cursor = cnx.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_name = cursor.fetchall()[0]

        self.df = pd.read_sql_query("SELECT * FROM noshow", cnx)

        self.logger.info(f"Size of DataFrame: {self.df.shape[0]}")

    def clean_data(self):
        self.logger.info("Starting data cleaning and Feature Engineering")
        self.df.dropna(subset=['no_show'], inplace=True)
        self.logger.info(f"Size of DataFrame: {self.df.shape[0]}")
        self.logger.info("na row dropped")
        self.df['price'] = self.df.apply(lambda x: cef.convertCurrencyStringToInt64(x['price']), axis=1)
        self.logger.info("price converted")
        self.df['room'] = self.df.apply(lambda x: cef.fillRoomUsingPrice(x['room'], x['branch'], x['price']), axis=1)
        self.logger.info("room na filled")
        self.df['arrival_month'] = self.df['arrival_month'].apply(cef.stringConvert)
        self.logger.info("arrival_month formatted")
        self.df['booked_months_before'] = self.df.apply(lambda x: cef.bookedMonthsBefore(x['booking_month'], x['arrival_month']), axis=1)
        self.logger.info("booked_months_before created")
        self.df.reset_index()
        self.logger.info("index reset")
        self.logger.info("Finished Data Cleaning and Feature Engineering")
        return self.df