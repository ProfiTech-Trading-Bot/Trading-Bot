#Fahim Ahmed, Hugh Jiang, Richard Yang, Zhi Rong Cai
#July 31st, 2021 - August 2nd, 2021
#ProfiTech Hackathon

#Set up the environment
from alpha_vantage.timeseries import TimeSeries
from api import ALPHA_VANTAGE_API_TOKEN
import numpy as np
import pandas as pd
import requests
import time

def getTrend(ticker):
    isUpTrend = False

    #Create TimeSeries object and make API call
    ts = TimeSeries(key = ALPHA_VANTAGE_API_TOKEN, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=ticker, interval ='60min', outputsize='full')

    #Reverse dataframe so most recent date is at the bottom
    data = data.iloc[::-1]

    #Get moving averages
    short_ma_period = 9
    short_ma_name = 'MA_' + str(short_ma_period)
    data[short_ma_name] = data.iloc[:,3].rolling(window=short_ma_period).mean()

    long_ma_period = 21
    long_ma_name = 'MA_' + str(long_ma_period)
    data[long_ma_name] = data.iloc[:,3].rolling(window=long_ma_period).mean()
    

    #If shorter period MA is higher than longer period, it means the price is trending upwards
    if data.iloc[-1][short_ma_name] > data.iloc[-1][long_ma_name]:
        isUpTrend = True
        

    return isUpTrend

print(getTrend('AMZN'))