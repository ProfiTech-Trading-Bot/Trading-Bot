def getStockPrice(ticker):
    return


def buyStock(ticker, quantity, balance):
    #if the user has enough funds for the trade, buy the stock
    if balance - quantity * getStockPrice(ticker) >= 0:
        #log the trade and update user's balance
        return balance - quantity * getStockPrice(ticker)
    #otherwise leave the balance unchanged
    return balance

def sellStock(ticker, quantity, balance):
    #if the user has enough shares for the trade, sell the stock
    #log the trade
    return balance

balance = 10000 #starting account balance of $10,000