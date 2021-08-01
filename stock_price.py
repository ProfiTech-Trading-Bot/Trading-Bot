#Fahim Ahmed, Hugh Jiang, Richard Yang, Zhi Rong Cai
#July 31st, 2021 - August 2nd, 2021 

#Set up the environment
from alpha_vantage.timeseries import TimeSeries
from api import ALPHA_VANTAGE_API_TOKEN, STOCK_SYMBOL
import numpy as np
import pandas as pd
import requests
import time

#Create TimeSeries object and make API call
ts = TimeSeries(key = ALPHA_VANTAGE_API_TOKEN, output_format='pandas')
data, meta_data = ts.get_intraday(symbol= STOCK_SYMBOL, interval ='5min', outputsize='full')


#Import data
print('\n')

#Reverse dataframe so most recent date is at the bottom
data = data.iloc[::-1]

#Get moving averages
short_ma_period = 9
short_ma_name = 'MA_' + str(short_ma_period)
data[short_ma_name] = data.iloc[:,3].rolling(window=short_ma_period).mean()


long_ma_period = 21
long_ma_name = 'MA_' + str(long_ma_period)
data[long_ma_name] = data.iloc[:,3].rolling(window=long_ma_period).mean()
 
print(data.tail())

#If shorter period MA is higher than longer period, it means the price is trending upwards
if data.iloc[-1][short_ma_name] > data.iloc[-1][long_ma_name]:
    print('Upward Trend')
    
elif data.ilc[-1][short_ma_name] < data.iloc[-1][long_ma_name]:
    print('Downward Trend')

else:
    print('Stationary Trend')
