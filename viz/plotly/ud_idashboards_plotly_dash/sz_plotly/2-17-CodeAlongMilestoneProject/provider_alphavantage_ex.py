import pandas as pd 
import pandas_datareader.data as web
import os 
import pandas_datareader.data as web
from datetime import datetime
from pprint import pprint as pp


os.environ["ALPHAVANTAGE_API_KEY"] = "BTXXQI1TJH56ZEJG"

tkr="AAPL"
tkr="AGNC"
tkr="TSLA"
tkr="MSFT"

start = datetime(2020, 1, 1)
end = datetime(2020, 5, 7)


df = web.DataReader(tkr, "av-daily",start=start,end=end )

pp(df.shape)
pp(df.tail)
