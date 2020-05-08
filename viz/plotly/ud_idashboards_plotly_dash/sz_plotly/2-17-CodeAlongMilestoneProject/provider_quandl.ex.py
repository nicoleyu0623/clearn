import pandas as pd 
import numpy as np 

import quandl as ql
from pprint import pprint as pp
import pandas_datareader.data as web
import os 

#quandl
os.environ["QUANDL_API_KEY"] ="dCbRAxPkcnxxxzTtDFW5"


start = '2019-01-01'
end = '2020-05-01'

symbol = 'IBM.US' 

df = web.DataReader(symbol, 'quandl', start, end)

pp(df.shape)
pp(df.tail())
