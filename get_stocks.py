import requests
import re
import yfinance as yf
import keys
import alpaca_trade_api as tradeapi
from bs4 import BeautifulSoup

api = tradeapi.REST(keys.PUBLIC_KEY, keys.PRIVATE_KEY, base_url='https://paper-api.alpaca.markets') # or use ENV Vars shown below
account = api.get_account()
#print(account)


soup = BeautifulSoup(requests.get("https://robinhood.com/collections/100-most-popular").content, 'html.parser')
#print(soup.prettify())
soup.prettify()

URL = "https://robinhood.com/collections/100-most-popular"

def get_stocks_dict():
    soup = BeautifulSoup(requests.get("https://robinhood.com/collections/100-most-popular").content, 'html.parser')
    soup.prettify()
    stock_dict = {}
    stock_names = []
    for stock in soup.find_all("a"):
        stockURL = stock.get('href')
        splitText = stockURL.split("/")
        if not stock_names.__contains__(splitText[len(splitText) - 1]):
            stock_names.append(splitText[len(splitText) - 1])

    buy_percents = soup.body.findAll(text=re.compile('% B'))
    for x in range(len(buy_percents)):
        stock_dict[stock_names[x]] = buy_percents[x].split("% ")[0]

    return stock_dict

def get_stock_prices():
    soup = BeautifulSoup(requests.get("https://robinhood.com/collections/100-most-popular").content, 'html.parser')
    soup.prettify()
    stock_prices = []
    for price in soup.body.findAll(text=re.compile('\$')):
        if "." in price:
            stock_prices.append(price)
    print(stock_prices)




tsla = yf.Ticker("TSLA")

