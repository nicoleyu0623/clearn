import pandas as  pd

from pprint import pprint as pp

import seaborn as sns
import matplotlib.pyplot as plt


"""
data 

airlines.csv - data on each airline.

country - where the airline is headquartered.
active - if the airline is still active.
airports.csv - data on each airport.

name - name of the airport.
city - city the airport is located.
country - country the airport is located.
code - unique airport code.
latitude - latitude value.
longitude - longitude value.
routes.csv - data on each flight route.

airline - airline for the route.
source - starting city for the route.
dest - destination city for the route.

"""

# questions to explore
# 1. For each airport, which destination airport is the most common?
# 2. Which cities are the most important hubs for airports and airlines?

alfn =  'openflights/airlines.csv'
apfn =  'openflights/airports.csv'
rtfn =  'openflights/routes.csv'

airlines = pd.read_csv(alfn)
airports = pd.read_csv(apfn)
routes = pd.read_csv(rtfn)

print(airlines.iloc[0,:])
print(airports.iloc[0,:])
print(routes.iloc[0,:])

