import yfinance as yf
import get_stocks

#0-100, at what buy percent should we buy
BUY_THRESHOLD = 75

def get_stocks_to_buy():
    stocks_dict = get_stocks.get_stocks_dict()
    stock_names = stocks_dict.keys()
    for name in stock_names:
        if int(stocks_dict[name]) >= BUY_THRESHOLD:
            print(name + " " + stocks_dict[name])
    print(stocks_dict)


