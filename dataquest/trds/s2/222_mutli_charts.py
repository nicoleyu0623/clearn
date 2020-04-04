import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint as pp

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

pp(unrate.head(5))



fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(unrate.loc[unrate.DATE.dt.year == 1948, 'DATE'],
         unrate.loc[unrate.DATE.dt.year == 1948, 'VALUE'])

ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate.loc[unrate.DATE.dt.year == 1949, 'DATE'],
         unrate.loc[unrate.DATE.dt.year == 1949, 'VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()



fig = plt.figure(figsize=(12, 12))
i = 1
for y in list(range(1948,1953)):
  ax_c = fig.add_subplot(5,1,i)
  ax_c.plot(unrate.loc[unrate.DATE.dt.year == y, 'DATE'],
           unrate.loc[unrate.DATE.dt.year == y, 'VALUE'])
  ax_c.set_title("Monthly Unemployment Rate, {0}".format(y))
  i += 1
plt.show()


#8
fig = plt.figure(figsize=(6, 3))
plt.plot(unrate.loc[unrate.DATE.dt.year == 1948, 'DATE'].dt.month,
         unrate.loc[unrate.DATE.dt.year == 1948, 'VALUE'], c="red")
plt.plot(unrate.loc[unrate.DATE.dt.year == 1949, 'DATE'].dt.month,
         unrate.loc[unrate.DATE.dt.year == 1949, 'VALUE'], c="blue")
plt.show()


#10
colors = ["red", "blue", "green", "orange", "black"]
i = 0
fig = plt.figure(figsize=(10, 6))
for y in list(range(1948,1953)):
    plt.plot(unrate.loc[unrate.DATE.dt.year == y, 'DATE'].dt.month,
             unrate.loc[unrate.DATE.dt.year == y, 'VALUE'], c=colors[i])
    i += 1
plt.show()

#11
fig = plt.figure(figsize=(10, 6))
colors = ["red", "blue", "green", "orange", "black"]
i = 0
for y in list(range(1948,1953)):
    plt.plot(unrate.loc[unrate.DATE.dt.year == y, 'DATE'].dt.month,
             unrate.loc[unrate.DATE.dt.year == y, 'VALUE'], c=colors[i], label=str(y))
    i += 1
plt.legend(loc='upper left')
plt.show()

#12
fig = plt.figure(figsize=(10, 6))
colors = ["red", "blue", "green", "orange", "black"]
i = 0
for y in list(range(1948,1953)):
    plt.plot(unrate.loc[unrate.DATE.dt.year == y, 'DATE'].dt.month,
             unrate.loc[unrate.DATE.dt.year == y, 'VALUE'], c=colors[i], label=str(y))
    i += 1
plt.legend(loc='upper left')
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.show()



