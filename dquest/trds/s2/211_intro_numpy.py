from banners import *
from pprint import pprint as pp
import csv
import numpy as np


# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

c_taxi_list = [ [ float(f) for f in r ] for r in taxi_list]

taxi = np.array(c_taxi_list)  #create numpy array


print(taxi.shape)


taxi_ten = taxi[:10]

pp(taxi_ten[:,0:2]) #take two first columns

pp(taxi_ten[[0,1,3],:]) # subset specific rows


row_0 = taxi[0,:]
rows_391_to_500 = taxi[391:501,:] #inclusive
row_21_column_5 = taxi[21, 5]

columns_1_4_7=taxi[:,[1,4,7]]
row_99_columns_5_to_8=taxi[99,5:9] #inclusing for column
rows_100_to_200_column_14=taxi[100:201,14]



trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]
trip_length_hours = trip_length_seconds / 3600
trip_mph = trip_distance_miles / trip_length_hours
trip_mph_a = np.divide(trip_distance_miles,  trip_length_hours)

pp(trip_mph[:10])
pp(trip_mph == trip_mph_a)

mph_mean=trip_mph.mean()
mph_max=trip_mph.max()
mph_min=trip_mph.min()
mph_sum=trip_mph.sum()
#trip_mph.median() #method does not exist
#or via import statistics as s

taxi.max(axis=0) # columns max
taxi.max(axis=1) #rows max

ones = np.array([ [1,1,1,1],
        [1,1,1,1] ])

zeros =np.array([ 0, 0, 0, 0])
zeros_2d = np.expand_dims(zeros,axis=0)
combined = np.concatenate([ones,zeros_2d],axis=0)

pp(combined)

trip_mph_2d = np.expand_dims(trip_mph,axis=1)
taxi = np.concatenate([taxi,trip_mph_2d],axis=1)

pp(taxi[:2])


fruit = np.array(['orange', 'banana', 'apple', 'cherry'])

sorted_order = np.argsort(fruit)


banner("sorting np array on given column")
i_sq = np.array([[5,2,8,3,4],[2,8,6,2,5],[1,6,2,7,7],[0,7,7,4,5],[5,7,1,1,2]])
pp(i_sq)

idx_srt = np.argsort(i_sq[:,4])

i_sq_srt = i_sq[idx_srt]
starprint('afer sorting on col 4')
pp(i_sq_srt)

starprint("sorting taxi on last column (added trip_mph")
ix = np.argsort(taxi[:,15])
taxi_sorted_by_avgspeed = taxi[ix]

pp(taxi_sorted_by_avgspeed)

