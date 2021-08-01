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
        #if the user already owns shares, calculate the average cost basis.
        if ticker in portfolio:
            initialQuantity = portfolio[ticker]['quantity']
            initialPrice = portfolio[ticker]['purchasePrice']
            price = (initialQuantity * initialPrice + quantity * price) / (initialQuantity + quantity) #cost basis price (total investment / total quantity)

        #log the trade and update user's balance
        portfolio[ticker] = {
                'quantity': quantity,
                'purchasePrice': price,
                'date': date
                }
        balance = balance - quantity * getStockPrice(ticker)
    
    return portfolio

#note: should the date also be updated in the portfolio?
def sellStock(ticker, quantity, portfolio):
    global balance
    price = getStockPrice(ticker)
    #if the user has enough shares for the trade, sell the stock
    if portfolio[ticker]['quantity'] - quantity >= 0:
        portfolio[ticker]['quantity'] -= quantity
        balance += quantity * price
    
    #if all shares were sold, delete it from the dictionary
    if portfolio[ticker]['quantity'] == 0:
        del portfolio[ticker]

    return portfolio

balance = 10000 #starting account balance of $10,000
portfolio = {}

portfolio = buyStock('AMD', 10, portfolio)
print(balance)
print(portfolio)

portfolio = sellStock('AMD', 10, portfolio)
print(balance)
print(portfolio)