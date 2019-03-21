
from pprint import pprint as pp

import pandas as pd
import numpy as np

f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan #put none to previous rank at zero

fifth_row = f500.iloc[5,:]
first_three_rows = f500.iloc[0:3,:]
first_seventh_row_slice  = f500.iloc[[0,6],0:5]


f500 = pd.read_csv("f500.csv")
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

sorted_emp = f500.sort_values("employees", ascending=False)

top5_emp = sorted_emp.iloc[:5,:]


### masking on  CA

usa = f500.loc[f500["country"] == "USA"] #filter usa rows
is_california = usa["hq_location"].str.endswith("CA")  #mask for cali  str.contains(), str.startswith()
usa[is_california].iloc[:5,[0,1,2,3,12]]


previously_ranked=f500["previous_rank"].notnull()

rank_change = f500[previously_ranked].loc[:,"rank"] \
            - f500[previously_ranked].loc[:,"previous_rank"]



cols = ["company", "revenues", "profits"]

big_rev_neg_profit = f500[ (f500.revenues > 100000) & (f500.profits < 0 )]

cols = ["company", "sector", "country"]
tech_outside_usa = f500[(f500.sector == "Technology" )  & ( f500.country != "USA" )].head(5)


f500["rank_change"] = rank_change

cols = ["company", "rank", "previous_rank", "rank_change" ]


## with for loop
top_employer_by_country = {}
countries = f500["country"].unique()
for c in countries:
    selected_rows = f500[f500["country"] == c]
    sorted_rows = selected_rows.sort_values("employees", ascending=False)
    top_employer = sorted_rows.iloc[0]
    employer_name = top_employer["company"]
    top_employer_by_country[c] = employer_name

pp(top_employer_by_country)

### a more pandas way intellingent way
cols = ['country', 'employees']
r = f500[cols].groupby("country").max()
l = f500[["country","company", "employees"]]
top_empl_by_ctr = pd.merge(l,r, on='employees')
pp(top_empl_by_ctr)



roa = f500["profits"] / f500["assets"]
f500["roa"] = roa

top_roa_by_sector = {}
sectors = f500.sector.unique()
for s in sectors:
    df_sector = f500[f500["sector"] == s]
    row_top_roa = df_sector.sort_values(by="roa", ascending=False).iloc[0]
    top_roa_by_sector[s]=row_top_roa["company"]

pp(top_roa_by_sector)

