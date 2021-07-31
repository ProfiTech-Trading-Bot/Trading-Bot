#Fahim Ahmed, Hugh Jiang, Richard Yang, Zhi Rong Cai
#July 31st, 2021 - August 2nd, 2021

from api import ALPHA_VANTAGE_API_TOKEN
import requests
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

API_KEY = 'ZSROA6Z2ZC1HD740'
ts = TimeSeries(key=API_KEY, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')

print('\n')
print(data)
