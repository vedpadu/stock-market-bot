import math

import yfinance as yf
import get_stocks
import json
import alpaca_trade_api as tradeapi
import keys

#0-100, at what buy percent should we buy
BUY_THRESHOLD = 75
#0-100 at what buy percent should we sell
SELL_THRESHOLD = 25
#number of stocks to manage
STOCK_TOTAL = 20
api = tradeapi.REST(keys.PUBLIC_KEY, keys.PRIVATE_KEY, base_url='https://paper-api.alpaca.markets') # or use ENV Vars shown below
account = api.get_account()


def get_stocks_to_buy():
    stocks_dict = get_stocks.get_stocks_dict()
    stock_names = stocks_dict.keys()
    stocks_to_buy_dict = {}
    for name in stock_names:
        if int(stocks_dict[name]) >= BUY_THRESHOLD:
            stocks_to_buy_dict[name] = stocks_dict[name]
    return stocks_to_buy_dict

def get_stock_prices_to_buy():
    stocks_dict = get_stocks.get_stocks_dict()
    stock_names = stocks_dict.keys()
    stock_prices = get_stocks.get_stock_prices()
    stocks_to_buy_prices = {}
    for name in stock_names:
        if int(stocks_dict[name]) >= BUY_THRESHOLD:
            stocks_to_buy_prices[name] = stocks_dict[name]
    return stocks_to_buy_prices


def get_stocks_to_sell():
    stocks_dict = get_stocks.get_stocks_dict()
    stock_names = stocks_dict.keys()
    stocks_to_sell_dict = {}
    for name in stock_names:
        if int(stocks_dict[name]) <= SELL_THRESHOLD:
            stocks_to_sell_dict[name] = stocks_dict[name]
    return stocks_to_sell_dict


def sell_stocks(current_stocks_dict):
    stocks_to_sell = get_stocks_to_sell()
    stocks_to_sell_names = stocks_to_sell.keys()
    current_stock_names = current_stocks_dict.keys()
    stocks_dict = get_stocks.get_stocks_dict()
    stock_names = stocks_dict.keys()
    stocks_to_remove = []
    for name in current_stock_names:
        if stocks_to_sell_names.__contains__(name):
            stocks_to_remove.append(name)
        elif not stock_names.__contains__(name):
            stocks_to_remove.append(name)

    for stock_to_remove in stocks_to_remove:
        api.submit_order(
            symbol=stock_to_remove,
            side='buy',
            type='market',
            qty=str(current_stocks_dict[stock_to_remove]),
            time_in_force='day',
        )
        current_stocks_dict.pop(stock_to_remove)

    return current_stocks_dict


def buy_stocks(current_stocks_dict):
    current_stock_names = list(current_stocks_dict.keys())
    number_stocks_to_buy = STOCK_TOTAL - len(current_stocks_dict.keys())
    stocks_to_buy = get_stocks_to_buy()
    stocks_to_buy_names = list(stocks_to_buy.keys())
    stock_prices = get_stocks.get_stock_prices()
    i = 0
    stocks_bought = 0
    total_money = float(account.buying_power)
    money_to_spend = total_money/30.0
    while i < len(stocks_to_buy_names) and stocks_bought < number_stocks_to_buy:
        if not current_stock_names.__contains__(stocks_to_buy_names[i]):
            price_per_stock = stock_prices[stocks_to_buy_names[i]]
            quantity_to_buy = int(math.floor(money_to_spend/float(price_per_stock)))
            current_stocks_dict[stocks_to_buy_names[i]] = quantity_to_buy
            api.submit_order(
                symbol=stocks_to_buy_names[i],
                side='buy',
                type='market',
                qty=str(quantity_to_buy),
                time_in_force='day',
            )

            stocks_bought += 1;
        i += 1

    return current_stocks_dict





