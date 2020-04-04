
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pprint import pprint as pp

# tutor from https://pandas.pydata.org/pandas-docs/stable/10min.html


## obj creation

s  = pd.Series([1,3,5,5,np.nan, 6,8])
pp(s)
pp(s.shape)



#create idx
dates = pd.date_range('20130101', periods=10)
pp(dates)

#create a data frame
df = pd.DataFrame(np.random.rand(10,4), index=dates, columns=list('ABCD'))
pp(df)
#normally distributed values
df = pd.DataFrame(np.random.normal(0,1,(10,4)), index=dates, columns=list('ABCD'))





#can also create Data frame from a dict
df2 = pd.DataFrame(
{
'A' : 1.,
'B' : pd.Timestamp('20130102'),
'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
'D' : np.array([3] * 4,dtype='int32'),
'E' : pd.Categorical(["test","train","test","train"]),
'F' : 'foo'
})

pp(df2)
pp(df2.dtypes)
pp(df2.shape)

##view data

df.head()

df.tail(3)
df.index

df.describe() # equiivalent to R summary

df.T # transpose

#by index
df.sort_index(axis=1,ascending=False) #not very clear
#by values
df.sort_values(by='B')

#selecting data
df.A
df['A']
df[['A','B']]
df[0:3] #subselects row
df['20130102':'20130104'] # islicing on index dates

#### select using labels
#select multi axis by label with loc cannot use int indexing
df.loc[:,['A','B']]
df.loc['20130102':'20130104',['A','B']]
df.loc['20130102',['A','B']] # one line
df.loc[dates[0:2],'A']


df.loc[dates[0],'A']
df.at[dates[0],'A'] #fast access same as previous

##by position
df.iloc[3] #4th row

df.iloc[0:2,0:3] #st 2 rows and first 3 columns
df.iat[1,1]  #fast access


df[df > 0] #filtering a dataframe


df2= df.copy()
#appending a column with specified values
df2['E'] = ['one', 'one','two','three','four','three', 'four', 'five', 'six', 'four']
#apending a column of zeroes
df2['F']= np.array([0] * df2.shape[0])

#### boolean indexing  on string values  isin !!
df2[df2['E'].isin(['two', 'four'])]  # filter on str values in column

#setting values
s1 = pd.Series( list(range(10)), index=dates )
df['G'] = s1 #add new column

df.at[dates[0],'A'] = 0

##flip all data frame positive values to necative
df3=df.copy()
df3[df3>0] = -df3

# this adds new column with Nan as default value
df1 = df.reindex(index=df.index, columns=list(df.columns) + ['E'])

df1.loc[dates[0:2],'E'] = 1 #sets two first rows E to 1

#this drop any row having a NaN in any column
df1.dropna(how='any')

#assigns to NaN a default value
df1.fillna(value=5)

pd.isna(df1) #boolean mask for nones

##operations

df.mean() # on columns
df.mean(1) # on rows

## inserts 2 NaN at the start of an array
s = pd.Series([1,3,5,np.nan,6,8, 9, 10, 11, 12], index=dates).shift(2)

##apply
df.apply(np.cumsum)  #on all columns
df.iloc[:,0:2].apply(np.cumsum) #on first two columns

#with lambda function
df.apply(lambda x: x.max() - x.min())


##histogramming
s = pd.Series(np.random.randint(0, 11, size=1000)).value_counts()
s.value_counts()
pp(s)

##methods on strings
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()


## merging data frames

df = pd.DataFrame(np.random.randn(10, 4))
pcs= [df[:3], df[3:7], df[7:]] #split df into subrows
#merge the back
pd.concat(pcs)

## sql style  cool on columns
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left,right,on='key')


##appending rows

df = pd.DataFrame(np.random.normal(0,1,(10,4)), index=dates, columns=list('ABCD'))
s = df.iloc[df.shape[0]-1] #last row

dfa = df.append(s) #appending the last row
df.append(s, ignore_index=True) #this converts index to ints

##grouping

df = pd.DataFrame({ 'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
                    'C' : np.random.randn(8),
                    'D' : np.random.randn(8)})

df.groupby('A').sum() #sums all numeric coluns grouped by col 'A'

df.groupby(['A','B']).sum()

##apply grouping on a subset of columns
df.loc[:,['A','C']].groupby('A').sum()


#### reshaping
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz','foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two','one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])

df2 = df[:4] #first 4 rows of multi indexed df

#The stack() method “compresses” a level in the DataFrame’s columns.
stacked = df2.stack()

stacked.unstack() #reverse op


### pivot tables

df = pd.DataFrame({ 'A' : ['one', 'one', 'two', 'three'] * 3,
                    'B' : ['A', 'B', 'C'] * 4,
                    'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                    'D' : np.random.randn(12),
                    'E' : np.random.randn(12)})
## this produces a pivot table,  column D is splitted and sorted according to 2D indexing
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])


##time series
rng = pd.date_range('1/1/2012', periods=100, freq='S') #100 seconds
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

ts.resample('5Min').sum()  ##group values by 1 min => two rows


rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')

ts = pd.Series(np.random.randn(len(rng)), rng)

ts_utc = ts.tz_localize('UTC')
ts_utc.tz_convert('US/Eastern')
ts_utc.tz_convert("CET")

##Converting between time span representations:

rng=pd.date_range('1/1/2012', periods=5, freq='M') #months
ts = pd.Series(np.random.randn(len(rng)), index=rng) #date at end of month

ps = ts.to_period()  #date as '2012-01'
pp(ps)

ps.to_timestamp() #date at strt of month


## categoricals

df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                          "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})

df["grade"] = df["raw_grade"].astype("category")  #neew col added
df["grade"].cat.categories = ["very good", "good", "very bad"] #better category names

df.sort_values(by="grade") #sorting on category

df.groupby("grade").size()  #counts of grade


##plotting
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts.plot()

###getting data in out

df = pd.DataFrame(np.random.normal(0,1,(10,4)), index=dates, columns=list('ABCD'))

df.to_csv('foo.csv')

dfr = pd.read_csv('foo.csv')


#hdf5 stores

#df.to_hdf('foo.h5','df')
#dfhdfr = pd.read_hdf('foo.h5','df')

#xls
df.to_excel('foo.xlsx', sheet_name='Sheet1')
dfxls = pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])


