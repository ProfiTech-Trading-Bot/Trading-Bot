#Fahim Ahmed, Hugh Jiang, Richard Yang, Zhi Rong Cai
#July 31st, 2021 - August 2nd, 2021

#Set up the environment
from alpha_vantage.timeseries import TimeSeries
from api import ALPHA_VANTAGE_API_TOKEN
import numpy as np
import pandas as pd
import requests
import time

#Constants
STOCK_SYMBOL = 'MSFT'

#Create TimeSeries object and make API call
ts = TimeSeries(key = ALPHA_VANTAGE_API_TOKEN, output_format='pandas')
data, meta_data = ts.get_daily(symbol = STOCK_SYMBOL)

#Import data
print('\n')
print(data)
print(meta_data)

