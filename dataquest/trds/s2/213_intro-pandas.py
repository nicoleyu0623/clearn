
from pprint import pprint as pp

import pandas as pd
import numpy as np

def load_header(filename, separator=','):
    cols = []
    with open(filename, mode="rt", encoding='utf-8') as f:
        chars = [line.split('\n')[0] for line in f.readlines()[0]]
    gchars = ''.join(chars)
    cols = gchars.split(separator)
    return cols

def get_colidx(colname, columns):
    ix = columns.index(colname)
    return ix


fn="f500.csv"

dt_head=load_header(fn)

pp(dt_head)

pp(get_colidx("profits", dt_head))


f500 = pd.read_csv(fn, index_col=0)

#pp(f500)

f500_type = type(f500)

f500_shape = f500.shape

pp(f500_shape)




f500_head = f500.head(6)
f500_tail = f500.tail(8)
print(f500.info())


industries = f500.loc[:,'industry']
previous = f500.loc[:,['rank','previous_rank','years_on_global_500_list']]
financial_data = f500.iloc[:,1:6]

countries = f500.country
revenues_years = f500.loc[:,['revenues','years_on_global_500_list']]
ceo_to_sector = f500.loc[:,'ceo':'sector']

ceos = f500["ceo"] #get one column

walmart = ceos['Walmart']
apple_to_samsung = ceos['Apple':'Samsung Electronics']
oil_companies = ceos[['Exxon Mobil','BP', 'Chevron']]


drink_companies = f500.loc[["Anheuser-Busch InBev", "Coca-Cola", "Heineken Holding"]]
big_movers = f500.loc[['Aviva','HP','JD.com','BHP Billiton']]
middle_companies=f500.loc['Tata Motors':'Nationwide',["rank", "country"]]



profits_desc = f500.profits.describe()
revenue_and_employees_desc = f500[["revenues","employees"]].describe()
all_desc = f500.describe()


top5_countries = f500["country"].value_counts().head(5)
top5_previous_rank = f500["previous_rank"].value_counts().head(5)
max_f500 = f500.max(numeric_only=True)

f500["revenues_b"] = f500["revenues"] / 1000
f500.loc["Dow Chemical","ceo"] = "Jim Fitterling"


kr_bool = f500["country"] == 'South Korea'
top_5_kr = f500[kr_bool][0:5]


msk =f500["previous_rank"] == 0
f500.loc[msk,"previous_rank"] = np.nan
f500["previous_rank"].value_counts(dropna=False).head()


f500.hq_location.value_counts().head(5)


#reread country
fn="f500.csv"
f500 = pd.read_csv(fn, index_col=0)

us_msk = f500["country"] == 'USA'

cities_usa = f500[us_msk].hq_location.value_counts().head(5)

sector_china = f500[f500.country == "China"].sector.value_counts().head(5)

mean_employees_japan = f500[f500.country == "Japan"].employees.mean()