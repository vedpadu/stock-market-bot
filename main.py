import requests
import re
import yfinance as yf
import alpaca_trade_api as tradeapi
from bs4 import BeautifulSoup

api = tradeapi.REST('PK7CSTG35RWQPZCLOFRO', 'j7V0zezls2H7TFgrlKNIRySGbuwWBlo5rWAXK9Kh', base_url='https://paper-api.alpaca.markets') # or use ENV Vars shown below
account = api.get_account()
print(account)

"https://robinhood.com/collections/100-most-popular"
soup = BeautifulSoup(requests.get("https://robinhood.com/collections/100-most-popular").content, 'html.parser')
#print(soup.prettify())
soup.prettify()

#for stock in soup.find_all("a"):
#    print(stock.get('href'))

for stock in soup.body.findAll(text=re.compile('% B')):
    print(stock)

tsla = yf.Ticker("TSLA")

print(tsla.info);
