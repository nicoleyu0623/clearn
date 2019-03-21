from pprint import pprint as pp

import pandas as pd


"""
the data cleansing plan:

* read data 
* looks at dimensions
* visulize  the head

"""


fn="autos.csv"
autos = pd.read_csv(fn,encoding="Latin-1")

pp(autos.head())

#best way to check presence of null NaN values
pp( autos.isnull().sum() )

#2
def camel_to_snake(text):
    import re
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

def clean_col(col):
    col = col.strip()
    col = col.replace("yearOfRegistration", "registration_year")
    col = col.replace("monthOfRegistration", "registration_month")
    col = col.replace("notRepairedDamage", "unrepaired_damage")
    col = col.replace("dateCreated", "ad_created")
    col = camel_to_snake(col)
    return col

autos.columns = [ clean_col(c) for c in autos.columns ]

pp(autos.columns)

##3
pp(autos.describe() )

autos.drop("nr_of_pictures",axis=1, inplace=True)

autos["price"] = autos["price"].str.split('$',expand=True).iloc[:,1].str.replace(',','').astype(float)
autos["odometer"] = autos["odometer"].str.replace("km",'').str.replace(',','').astype(float)
autos.rename(columns={'odometer':'odometer_km'}, inplace=True)

pp(autos.describe())


#lets explore the high end of prices
autos[autos.price > 500000].loc[:,["name", "odometer_km","price" ]]

autos[((autos.price > 500000) & ~(autos.name.str.contains("Ferrari")) )]
#dropping thos values except  for ferraris
autos=autos[~((autos.price > 500000) & ~(autos.name.str.contains("Ferrari")) )] #antimasking

pp(autos.shape) #stripped off 12 rows

autos["ad_created"] = pd.to_datetime(autos["ad_created"])
autos["last_seen"] = pd.to_datetime(autos["last_seen"])

autos["ad_created_year"] = autos["ad_created"].dt.year
autos["ad_created_month"] = autos["ad_created"].dt.month

pp( autos.registration_year.describe() )

autos[autos.registration_year < 1920]
#unrealistic rows with high registration_year date
autos[autos.registration_year > 2016]
#keeping rows with sensible registration date
autos = autos[autos.registration_year.between(1920,2016)]
autos.shape


##lets explore data by brands
autos.brands.value_count(normalize=True)

cols=["brand", "price", "odometer_km", "registration_year"]

brand_stats = autos[cols].groupby("brand").mean()

brand_stats.sort_values(by=["price", "odometer_km"],ascending=False)