#Fahim Ahmed, Hugh Jiang, Richard Yang, Zhi Rong Cai
#July 31st, 2021 - August 2nd, 2021
#ProfiTech Hackathon

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import datetime
from alpha_vantage.timeseries import TimeSeries
from api import ALPHA_VANTAGE_API_TOKEN
from sentimental_analysis import TweetAnalyzer
from stock_price import getTrend


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
    global profitLog
    price = getStockPrice(ticker)
    date = datetime.datetime.now()
    #if the user has enough shares for the trade, sell the stock
    if portfolio[ticker]['quantity'] - quantity >= 0:
        portfolio[ticker]['quantity'] -= quantity
        balance += quantity * price
        
        #calculate profit from sale
        profit = quantity * price - quantity * portfolio[ticker]['purchasePrice']
        profitLogUpdate = pd.DataFrame({'profit': [profit], 'date': [date]})
        profitLog = profitLog.append(profitLogUpdate)
    
    #if all shares were sold, delete it from the dictionary
    if portfolio[ticker]['quantity'] == 0:
        del portfolio[ticker]

    return portfolio

#Graphs a chart of the trading bot's profit
def graphProfit():
    profitLog.plot(x = 'date', y = 'profit', kind = 'line')
    plt.title("Trading Bot Profit Overtime")
    plt.ylabel("Profit ($)")
    plt.xlabel("Date")
    plt.savefig('profit.png')

#Checks if a stock the user entered is one of the top 500 stocks.
def searchStocks(query):
    stocks = pd.read_csv("stocks_list.csv")
    stocks = stocks['Ticker'].tolist()

    return query.upper() in stocks


balance = 10000 #starting account balance of $10,000
profitLog = pd.DataFrame(columns = ['profit', 'date'])
initial = pd.DataFrame({'profit': [0], 'date': [datetime.datetime.now()]})
profitLog = profitLog.append(initial)

portfolio = {}

#portfolio = buyStock('AMD', 10, portfolio)
#portfolio = sellStock('AMD', 10, portfolio)

#graphProfit()

#print(checkStock("AAPL"))

