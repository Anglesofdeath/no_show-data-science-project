import numpy as np

def fillRoomUsingPrice(room: str, branch: str, price: float):
    '''
    this function takes the price of the room and the branch and if the room type falls within certain price ranges, it will fill in the room type. 
    '''
    orchard_list = [900.19, 913.17, 1200.03, 1217.58, 1521.98, 1800.85]
    changi_list = [600.15, 608.76, 800.03, 811.75, 1014.69, 1232.14]
    if room == None:
        if branch == 'Orchard':
            my_price = min(orchard_list, key = lambda x:abs(x-price)) #my_price is equal to the value in orchard_list that price is closest to (by finding the min difference between the boundary and price)
            if my_price == 900.19:
                return 'Single'
            if my_price == 913.17 or my_price == 1200.03:
                return 'Queen'
            if my_price == 1217.58 or my_price == 1521.98:
                return 'King'
            if my_price == 1800.85:
                return 'President Suite'

        if branch == 'Changi':
            my_price = min(changi_list, key = lambda x:abs(x-price))#my_price is equal to the value in changi_list that price is closest to (by finding the min difference between the boundary and price)
            if my_price == 600.15:
                return 'Single'
            if my_price == 608.76 or my_price == 800.03:
                return 'Queen'
            if my_price == 811.75 or my_price == 1014.69:
                return 'King'
            if my_price == 1232.14:
                return 'President Suite'    
    return room

def convertCurrencyStringToInt64(price):
    '''
    Takes a price(string) in either USD$ or SGD$ and returns the price in SGD$ without the SGD$ prefix. If no currency in input returns input
    '''
    str(price).replace(" ", "") #remove white spaces
    if str(price)[:4] == "USD$":
        return np.round(float(str(price)[4:]) *1.39, 2) #multiply if price is in USD; keeping it to 2 decimals as its a price
    if str(price)[:4] == "SGD$":
        return np.round(float(str(price)[4:]), 2) #price is in SGD; keeping to 2 decimals as its a price
    return price

def stringConvert(month: str):
    '''
    this function takes a string and returns the string with just the first letter capitalized. String must have minimum length = 1
    '''
    month = month.lower()
    return month[0].upper() + month[1:]

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def bookedMonthsBefore(booked_month: str, checkIn_month: str):
    '''
    this function will return the number of months between 2 given months inclusive of earlier month. Assumed that the difference is less than 1 year 
    and that the first variable is the earlier month and the second variable is later month.
    '''
    x = month_list.index(booked_month)
    y = month_list.index(checkIn_month)
    if y >= x:
        return y - x
    else:
        return 12 -(x - y)