from banners import *
from pprint import pprint as pp
import csv
import numpy as np

"""
nyc_taxis.csv dataset

pickup_year - The year of the trip.
pickup_month - The month of the trip (January is 1, December is 12).
pickup_day - The day of the month of the trip.
pickup_location_code - The airport or borough where the the trip started, as one of eight categories:
0 - Bronx.
1 - Brooklyn.
2 - JFK Airport.
3 - LaGuardia Airport.
4 - Manhattan.
5 - Newark Airport.
6 - Queens.
7 - Staten Island.
dropoff_location_code - The airport or borough where the the trip finished, using the same eight category codes as pickup_location_code.
trip_distance - The distance of the trip in miles.
trip_length - The length of the trip in seconds.
fare_amount - The base fare of the trip, in dollars.
total_amount - The total amount charged to the passenger, including all fees, tolls and tips.

"""

taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')
pp(taxi)

taxi.dtype
taxi = taxi[1:]

a = np.array([2,4,6,8])
ix = a < 5 # produces a boolean index
a[ix] #is a filtered np.array

banner('how to filter on a column')
i_sq = np.array([[5,2,8,3,4],[2,8,6,2,5],[1,6,2,7,7],[0,7,7,4,5],[5,7,1,1,2]])
pp(i_sq)
ix = i_sq[:,4] < 5 # we sort on the last column, index = 4, it produces a boolean filter
i_sq_filtered = i_sq[ix]
starprint('after filtering')
pp(i_sq_filtered) # contains only rows for which the 4th column < 5


a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = a < 3

b_bool = b == "blue"

c_bool = c > 100

taxi_head = ['pickup_year','pickup_month','pickup_day','pickup_dayofweek','pickup_time','pickup_location_code','dropoff_location_code','trip_distance','trip_length','fare_amount','fees_amount','tolls_amount','tip_amount','total_amount','payment_type']


pickup_month_ix = taxi_head.index('pickup_month')
pickup_month = taxi[:,pickup_month_ix] #2nd column of the whole dataset

january_bool = pickup_month == 1 #creates a bool index
january = pickup_month[january_bool]  # elements fro all pickup months only from january

january_rides = january.shape[0] # get number of rows (vec lenght) = number of raids in jan
print('raids in jan', january_rides)

## for feb

february_bool = pickup_month == 2 #creates a bool index
february = pickup_month[february_bool]  # elements fro all pickup months only from january
february_rides = february.shape[0]
print(february_rides)


march_bool = pickup_month == 3
march = pickup_month[march_bool]
march_rides = march.shape[0]
print(march_rides)


arr = np.array( [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

bl_1 = [True, False, True, True]

arr[bl_1] #uses index on rows as index length = row length

#arr[:,bl_1] #fails on mismatched dimensions

bl_2 = [False, True, True]

arr[:,bl_2] # ok, filtering specified columns


banner("how to filter out tax data rows with unrealistic speeds")

trip_mph = taxi[:,7] / ( taxi[:,8] / 3600 )
trip_mph_bl = trip_mph > 10000

trips_over_high = taxi[trip_mph_bl,5:9] #subcolumns 5 to 9

print(trips_over_high)

pp(taxi_head)

##find rows with highest tip amounts

tips = taxi[:,12]
tip_bool = tips > 50

top_tips = taxi[tip_bool, 5:14]

print(top_tips)

taxi_modified = taxi.copy()


taxi_modified[28214,5] = 1
taxi_modified[:,0] = 16
taxi_modified[1800:1802,7] = taxi_modified[:,7].mean()



a = np.array([1, 2, 3, 4, 5])

a[a>2] = 99

print(a)

#how to assign values to specific column
c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])


#first column c[:,1]>2 is a filter
c[c[:,1] > 2, 1] = 99


## append new column
newcol = np.zeros((taxi_modified.shape[0],1 ))
taxi_modified = np.append(taxi_modified,newcol,axis=1)

taxi_modified[taxi_modified[:,5]==2,15] = 1 #assign 1 based on filter
taxi_modified[taxi_modified[:,5]==3,15] = 1 #assign 1 based on filter
taxi_modified[taxi_modified[:,5]==5,15] = 1 #assign 1 based on filter



##challenges

jfk=taxi[taxi[:,5]==2,:]
laguardia=taxi[taxi[:,5]==3,:]
newark=taxi[taxi[:,5]==5,:]


jfk_count = taxi[taxi[:,6]==2,:].shape[0]
laguardia_count = taxi[taxi[:,6]==3,:].shape[0]
newark_count = taxi[taxi[:,6]==5,:].shape[0]

pp(jfk_count)
pp(laguardia_count)
pp(newark_count)

##challenge to remove the bad data

trip_mph = taxi[:,7] / ( taxi[:,8] / 3600 )

cleaned_taxi = taxi[trip_mph < 100,:]

mean_distance = cleaned_taxi[:,7].mean()
mean_length   = cleaned_taxi[:,8].mean()
mean_total_amount   = cleaned_taxi[:,13].mean()
mean_mph   = trip_mph[trip_mph < 100].mean()



