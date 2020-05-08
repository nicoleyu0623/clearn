import pandas as pd 
import pandas_datareader.data as web
import os 
from datetime import datetime
from pprint import pprint as pp

#os.environ["IEX_API_KEY"] = "pk_f31efdcc4d7d4726840c2d6ddd172cb1"

start = datetime(2018, 1, 1)
end = datetime(2020, 5, 7)
df = web.DataReader('TSLA', 'yahoo', start, end)
pp(df.shape)
pp(df.tail())
