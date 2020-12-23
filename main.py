import get_stocks
import buy_sell_stocks

#get_stocks.init_json()
#buy_sell_stocks.get_stocks_to_buy()
#print(get_stocks.get_stock_prices())
current_stocks = get_stocks.get_current_stocks()
current_stocks = buy_sell_stocks.sell_stocks(current_stocks)
current_stocks = buy_sell_stocks.buy_stocks(current_stocks)
get_stocks.upload_current_stocks(current_stocks)
print(current_stocks)
