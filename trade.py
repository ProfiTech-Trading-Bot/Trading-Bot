import pandas as pd
import datetime
from alpha_vantage.timeseries import TimeSeries
from api import ALPHA_VANTAGE_API_TOKEN

def getStockPrice(ticker):
    #Create TimeSeries object and make API call
    ts = TimeSeries(key = ALPHA_VANTAGE_API_TOKEN, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=ticker, interval='5min', outputsize='full')
    recentClose = data.iloc[0, 3] #newest value in the 0th row from the 'close' column
    return recentClose

def buyStock(ticker, quantity, portfolio):
    global balance
    price = getStockPrice(ticker)
    date = datetime.datetime.now()
    #if the user has enough funds for the trade, buy the stock
    if balance - quantity * price >= 0:
        #log the trade and update user's balance
        trade = pd.DataFrame({'ticker': [ticker],
                                'quantity': [quantity],
                                'purchasePrice': [price],
                                'date': [date]})
        portfolio = portfolio.append(trade)
        balance = balance - quantity * getStockPrice(ticker)

    return portfolio

def sellStock(ticker, quantity, balance):
    #if the user has enough shares for the trade, sell the stock
    #log the trade
    return balance

balance = 10000 #starting account balance of $10,000
portfolio = pd.DataFrame(columns=['ticker', 'quantity', 'purchasePrice', 'date'])
#portfolio2 = {}

portfolio = buyStock('AMD', 10, portfolio)

print(balance)
print(portfolio.head())