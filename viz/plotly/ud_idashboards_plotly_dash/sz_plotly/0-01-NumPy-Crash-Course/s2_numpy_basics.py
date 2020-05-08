import numpy as np 
from pprint import pprint as pp


### create numpy array
mylist=[1,2,3,4]
ar=np.array(mylist)
type(mylist) #stil a list
type(ar)

## create a seq
a = np.arange(0,10)

a= np.arange(0,10,2) #step 2

##### create 2 dim array of zeros
###################################
z=np.zeros((5,5))

np.zeros((1,10))  #10cols      
#vs
np.zeros((10,1)) #10 rows


np.ones((3,3))  # 3x3 of 1


#### create random arrays
#########################
np.random.randint(0,100)

np.random.randint(0,100,(5,5))  # 5x5 metrics of random ints


##### linearly spaced arrays
#########################
np.linspace(0,10,6) #6 numbers between 0 and 10, equal spaces between them
np.linspace(0.1,10,100) #creates an array of 100 els between 0 and 10 with step 0.1

#### Numpy Operations #########
##############################
np.random.seed(101)
arr = np.random.randint(0,100,10)
arr.max()
arr.min()
arr.mean()
arr.std()

arr.argmax() #index for max
arr.argmin() #index for min

### change dimensions from 1 to 
arr.reshape(2,5) 


#### Indexing ############
#########################
mat = np.arange(0,100).reshape(10,10)

mat[5,2] #52  5th row 3rd column

mat[0,:] #first row
mat[1,:] #2nd row
mat[:,0] #first col
##########################
#  replicate element #
##########################
ntimes=4
val=3
a=np.repeat(val, ntimes)

##########################
#  masking #
##########################
#mask is a matrix of boolean values
mat>50
#mask applied to a 2d value returns an index of machating elements
mat[mat>50]



