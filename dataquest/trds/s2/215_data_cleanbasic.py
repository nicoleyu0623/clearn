from pprint import pprint as pp

import pandas as pd
import numpy as np


"""
scope
* Clean columns names.
* Extract and convert numeric values from string values.
* Extract string data.
* Work with missing values.
"""
fn="laptops.csv"
laptops = pd.read_csv(fn,encoding="Latin-1")
#laptops.index.name = None

pp(laptops.info())
pp(laptops.columns)

def clean_col(col):
    col = col.strip()
    col = col.replace("(","")
    col = col.replace(")","")
    col = col.replace("Operating System", "OS")
    col = col.replace(" ", "_")  #replace spaces in col names with _
    col = col.lower()
    return col

laptops.columns = [ clean_col(c) for c in laptops.columns ]

pp(laptops.columns)

""" 
workflow to cleaning a data in column
- look in data head 
- detect patterns and special cases
- remove non-digit characters
- rename columns if required 
- convert the column to a numeric dtype 
"""

laptops["screen_size"] = laptops["screen_size"].str.replace('"','')
laptops["screen_size"] = laptops["screen_size"].astype(float)
#changing column name
laptops.rename({"screen_size": "screen_size_inches"}, axis=1, inplace=True)
pp(laptops.info())


laptops["ram"] = laptops["ram"].str.replace('GB','')
laptops["ram"] = laptops["ram"].astype(int)
laptops.rename({"ram": "ram_gb"}, axis=1, inplace=True)
print(laptops.info())



pp( laptops[laptops.weight.str.contains("kgs")] ) ##4s is a bad value seen in exception
 # => remove kgs before kg

#4
laptops["weight"] = laptops["weight"].str.replace("kgs","")
laptops["weight"] = laptops["weight"].str.replace("kg","")
laptops["weight"] = laptops["weight"].astype(float)
laptops.rename({"weight": "weight_kg"}, axis=1, inplace=True)

laptops["price_euros"] = laptops["price_euros"].str.replace(',','.')
laptops["price_euros"] = laptops["price_euros"].astype(float)

weight_describe = laptops.weight_kg.describe()
price_describe = laptops.price_euros.describe()

pp(weight_describe)
pp(price_describe)

#5
## factor out gpu or cpu manufacturers
laptops["gpu_manufacturer"] = (laptops["gpu"].str.split(n=1,expand=True)
                                   .iloc[:,0])

laptops["cpu_manufacturer"] = (laptops["cpu"].str.split(n=1,expand=True)
                                    .iloc[:,0])


#6
screen_res = laptops["screen"].str.rsplit(n=1, expand=True)
screen_res.columns = ["A", "B"]
screen_res.loc[ screen_res.B.isnull(), 'B'] = screen_res['A'] #clever assigning
#pp(screen_res.head(10))

cpu_ghz = laptops.cpu.str.rsplit(n=1, expand=True).iloc[:,1]
laptops["cpu_speed"] = cpu_ghz.str.replace('GHz', '').astype(float)


#7 !!powerful multiple corrections in a column

pp(laptops.os.value_counts())
mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows', #ok for rerun
    'macOS': 'macOS'  #ok for rerun
}

## powerful
laptops["os"] = laptops["os"].map(mapping_dict)
pp(laptops.os.value_counts())

#8
#best way to check presence of null NaN values
pp( laptops.isnull().sum() )

#1st method drop all rows containing NaN in any feature
laptops_no_null_rows = laptops.dropna()
#remove any columns which contain Nan
laptops_no_null_cols = laptops.dropna(axis=1)

#9 replacing nas with a value
pp( laptops.os_version.value_counts() )
pp( laptops.loc[laptops["os_version"].isnull(),"os"] ) #see os with no os_version

#fixing macos
pp(laptops.loc[laptops.os =="macOS", ["os", "os_version"] ].head(10) )
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"

#fixing no os
laptops.loc[laptops["os"] == "No OS", "os_version"] = "Version Unknown"

value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()

#10 challenge  "storage"


scols =  laptops["storage"].str.split('+', expand=True)
scols.columns = ["store1", "store2"]

##main logic per storage 1 or 2
def proc_store(column):
    column = column.str.strip()
    #import pdb
    #pdb.set_trace()
    column = column.str.replace("Flash Storage", "Flash_Storage")
    spars = column.str.split(expand=True)
    spars.iloc[:, 1] = spars.iloc[:, 1].str.replace("Flash_Storage", "Flash Storage")
    spars.columns = ["size", "type"]
    tbmsk = (spars["size"].str.contains("TB") ) & (spars["size"].isnull() == False)
    spars.loc[tbmsk, "is_tb"] = True
    spars["size"] = spars["size"].str.replace("GB","")
    spars["size"] = spars["size"].str.replace("TB", "")
    spars["size"] = spars["size"].astype(float)
    spars.loc[ spars["is_tb"] == True, "size" ]  = spars["size"] * 1000
    return spars.iloc[:,:2]

pars1= proc_store(scols["store1"])
pars1.columns = ["storage_1_capacity_gb","storage_1_type"]


pars2= proc_store(scols["store2"])
pars2.columns = ["storage_2_capacity_gb","storage_2_type"]

laptops = pd.concat([laptops, pars1, pars2],axis=1)
laptops = laptops.drop("storage", axis=1)

########################
## reference solution
#######################

# # replace 'TB' with 000 and rm 'GB'
# laptops["storage"] = laptops["storage"].str.replace('GB','').str.replace('TB','000')
#
# # split out into two columns for storage
# laptops[["storage_1", "storage_2"]] = laptops["storage"].str.split("+", expand=True)
#
# for s in ["storage_1", "storage_2"]:
#     s_capacity = s + "_capacity_gb"
#     s_type = s + "_type"
#     # create new cols for capacity and type
#     laptops[[s_capacity, s_type]] = laptops[s].str.split(n=1,expand=True)
#     # make capacity numeric (can't be int because of missing values)
#     laptops[s_capacity] = laptops[s_capacity].astype(float)
#
# # remove unneeded columns
# laptops.drop(["storage", "storage_1", "storage_2"], axis=1, inplace=True)

#10
#rearranged columns
cols = ['manufacturer', 'model_name', 'category', 'screen_size_inches',
        'screen', 'cpu', 'cpu_manufacturer',  'cpu_speed', 'ram_gb',
        'storage_1_type', 'storage_1_capacity_gb', 'storage_2_type',
        'storage_2_capacity_gb', 'gpu', 'gpu_manufacturer', 'os',
        'os_version', 'weight_kg', 'price_euros']

fn = "laptops_cleaned.csv"
laptops = laptops[cols] #reorder by new column list
laptops.to_csv(fn, index=False)

laptops_cleaned = pd.read_csv(fn)
laptops_cleaned_dtypes = laptops[cols].dtypes
