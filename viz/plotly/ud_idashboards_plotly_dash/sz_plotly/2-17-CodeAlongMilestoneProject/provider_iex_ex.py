import pandas as pd 
import os 
from datetime import datetime
from pprint import pprint as pp
from iexfinance.stocks import get_historical_data

os.environ["IEX_TOKEN"] = "pk_f31efdcc4d7d4726840c2d6ddd172cb1"

start = datetime(2018, 1, 1)
end = datetime(2020, 5, 7)
stock_ticker='IBM'
df = get_historical_data(stock_ticker, start=start, end=end,
                     close_only=True, output_format='pandas')
pp(df.shape)
pp(df.head(3))
pp(df.tail(3))
