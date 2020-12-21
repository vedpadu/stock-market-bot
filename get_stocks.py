import requests
import re
import yfinance as yf
import alpaca_trade_api as tradeapi
from bs4 import BeautifulSoup

api = tradeapi.REST('PK7CSTG35RWQPZCLOFRO', 'j7V0zezls2H7TFgrlKNIRySGbuwWBlo5rWAXK9Kh', base_url='https://paper-api.alpaca.markets') # or use ENV Vars shown below
account = api.get_account()
print(account)


soup = BeautifulSoup(requests.get("https://robinhood.com/collections/100-most-popular").content, 'html.parser')
#print(soup.prettify())
soup.prettify()

URL = "https://robinhood.com/collections/100-most-popular"

def get_stocks():
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

    print(stock_dict)




tsla = yf.Ticker("TSLA")

print(tsla.info);