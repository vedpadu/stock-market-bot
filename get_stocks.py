import requests
import re
import yfinance as yf
import keys
import alpaca_trade_api as tradeapi
from bs4 import BeautifulSoup
import json


#print(account)


def get_current_stocks():
    with open('current_stocks.json') as f:
        data = json.load(f)
        return data


def upload_current_stocks(current_stocks_dict):
    with open('current_stocks.json', 'w') as f:
        json.dump(current_stocks_dict, f)

def get_stocks_dict():
    soup = BeautifulSoup(requests.get(keys.URL).content, 'html.parser')
    soup.prettify()
    stock_dict = {}
    stock_names = []
    for stock in soup.find_all("a"):
        stock_url = stock.get('href')
        split_text = stock_url.split("/")
        if not stock_names.__contains__(split_text[len(split_text) - 1]):
            stock_names.append(split_text[len(split_text) - 1])

    buy_percents = soup.body.findAll(text=re.compile('% B'))
    for x in range(len(buy_percents)):
        stock_dict[stock_names[x]] = buy_percents[x].split("% ")[0]

    return stock_dict


def get_stock_prices():
    soup = BeautifulSoup(requests.get(keys.URL).content, 'html.parser')
    soup.prettify()
    stock_names = list(get_stocks_dict().keys())
    stock_prices = {}
    x = 0
    for price in soup.body.findAll(text=re.compile('\$')):
        if "." in price:
            if x < len(stock_names):
                price = price.replace(',', '')
                price_split_string = price.split('$')
                stock_prices[stock_names[x]] = float(price_split_string[len(price_split_string)-1])
                x += 1

    return stock_prices


