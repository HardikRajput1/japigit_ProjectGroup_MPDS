# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 12:34:15 2021

@author: HR SINGH
"""
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

API_KEY = '1JY2C3Z3716I4Y95'


def getStockdata(symbol):
    try:
        print("Please wait for a sec, we are fetching the data for you. \n")
        ts = TimeSeries(key=API_KEY, output_format='pandas')

        data, meta_data = ts.get_intraday(symbol=symbol, interval='1min')

        return str(data.tail(1).iloc[0]['4. close'])

    except:
        return "Data not found"


def main():
    f = open('japi.out', 'w')
    while 1:
        user_input = input("Enter the name of the symbol to get its current share price, or type QUIT to exit : \n").upper()
        if user_input != "QUIT":
            response = 'The current share price of the {} is {}\n'.format(user_input, getStockdata(user_input))
            print(response)
            f.write(response)
            print("Stock Quotes retrieved successfully!")
        else:
            raise SystemExit


main()