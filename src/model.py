import logging

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection._split import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


class Model:
    def __init__(self, data) -> None:
        self.data = data

        self.logger = logging.getLogger(__name__)

    def build_model(self):
        drop_columns_name = ["price", "no_show", "platform", "checkout_month", "booking_month", "num_adults", "checkout_day", "booking_id", "arrival_day"]
        X = self.data.drop(drop_columns_name, axis = 1)

        y = self.data["no_show"]

        self.logger.info(f"y shape: {y.shape}")

        enc = OneHotEncoder(handle_unknown="ignore")
        encoder_df = pd.DataFrame(enc.fit_transform(X[['branch', 'first_time', 'country', 'room', 'arrival_month']]).toarray())
        X.reset_index()
        encoder_df.reset_index()
        X = X.join(encoder_df)
        X = X.drop(['branch', 'first_time', 'country', 'room', 'arrival_month'], axis = 1)
        X_train, X_test, y_train, y_test = train_test_split(
            encoder_df, y, test_size=0.2, random_state=2
        )
        #X_train = X_train.to_numpy()

        clf = RandomForestClassifier(random_state=42)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        self.logger.info(f1_score(y_test, y_pred, average="macro"))
        self.logger.info(precision_score(y_test, y_pred, average="macro"))
        self.logger.info(recall_score(y_test, y_pred, average="macro"))

        unique, counts = np.unique(y_pred, return_counts=True)

        result = np.column_stack((unique, counts))
        self.logger.info(result)