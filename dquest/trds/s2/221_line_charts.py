import pandas as pd

from pprint import pprint as pp

import matplotlib.pyplot as plt



fn="unrate.csv"
unrate = pd.read_csv(fn)
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

pp(unrate.head(12))

#plt.plot()
#plt.show()


#plt.plot(list(range(10)) ,[l*l for l in list(range(10)) ] )
#plt.show()


plt.plot( unrate.loc[:11,'DATE'], unrate.loc[:11,'VALUE'] )
plt.show() #unemployment for 1948


plt.plot( unrate.loc[:11,'DATE'], unrate.loc[:11,'VALUE'] )
plt.xticks(rotation='vertical')
plt.show() #unemployment for 1948



plt.plot( unrate.loc[:11,'DATE'], unrate.loc[:11,'VALUE'] )
plt.xticks(rotation='vertical')
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show() #unemployment for 1948





