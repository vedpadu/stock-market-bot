import get_stocks
import buy_sell_stocks
from datetime import datetime
import pytz

last_date_time_run = None
HAS_RUN = False

while True:
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)

    current_time = datetime_NY.strftime("%H:%M:%S")
    if 0 <= datetime_NY.weekday() <= 4:
        if not HAS_RUN:
            current_stocks = get_stocks.get_current_stocks()
            current_stocks = buy_sell_stocks.sell_stocks(current_stocks)
            current_stocks = buy_sell_stocks.buy_stocks(current_stocks)
            get_stocks.upload_current_stocks(current_stocks)
            print(current_stocks)
            print(current_time)
            HAS_RUN = True
        else:
            if datetime_NY.minute == 0:
                if last_date_time_run is None:
                    HAS_RUN = False
                    last_date_time_run = datetime.now()
                else:
                    diff_datetime = datetime.now() - last_date_time_run
                    if diff_datetime.seconds >= 60 * 60:
                        HAS_RUN = False
                        last_date_time_run = datetime.now()
                        print(last_date_time_run)




