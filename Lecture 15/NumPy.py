# Data Manipulation and analysis with NumPy

#Definition: NumPy is a fundamental package for scientific computing With Python. tt provides support for arrays, matrices. and a large
#collection of mathematical functions to operate on these data structures. NumPy arrays are mote efficient and provide better performance for
#numerical operations compared to Python's built-in lists.
#use Case in Real Life: NumPy can be used in various scientific computing scenarios. such as statistical analysis. signal processing, and image
#processing.

# numpy is a library
import numpy as np   # renaming numpy as np to use conveniently

# creating a 1D array from a list
arr1=np.array([1,2,3,4,5])
print(arr1)

# creating a 2D array from a list of lists
arr2=np.array([[1,2,3,],[4,5,6]])
print(arr2)

# creating arrays with functions
zeroes=np.zeros((3,4))   # matrix of 0s
print(zeroes)

ones=np.ones((10,10))
print(ones)

# creating an array with a range of values
range_arr=np.arange(10,20,2)   # array starting from 10 till 20 with a gap of 2
print(range_arr)

# creating an array with random values
random_arr=np.random.rand(3,3)  # this keeps on changing on every run
print(random_arr)

# Basic array operations: Element-wise operations

print(arr1[1])

#mathematical operations
for i in arr1:
    print(i)
print("\n")

#element-wise addition
for i in arr1:
    print(i+2)
    
print("\n")

#using numpy
print(arr1+2)

# element wise multiplication
for i in arr1:
    print(i*2)

#using numpy
print(arr1*2)

#mathematical functions
print(np.sqrt(arr1))  #square root of elements
print(np.exp(arr1))  #e^arr1[i]
print(np.log(arr1))
print(np.sin(arr1))

# indexing and slicing-indexing
print(arr1[0])  #first element
print(arr1[-1])  #last element using negative indexing

# slicing
print(arr1[1:4])  #prints elements from 1 to 3
print(arr1[:3])   #prints first three elements
print(arr1[2:])   #prints elements from 2nd index till last

#advanced indexing
#boolean indexing
print(arr1[arr1>3])  # prints only elements of the array that are greater than 3

#fancy indexing
indices=[0,2,4]
print(arr1[indices])
print("\n")
#reshaping and transposing
arr=np.array([[1,2,3],[4,5,6]])  # two rows and three columns
print(arr)
print("\n")
#reshaping arrays
reshaped=arr.reshape((3,2))  # 3 rows and 2 columns
print(reshaped)
# rows of original should be equal to columns in reshaped and vice versa
print("\n")
#transposing arrays
transpose=arr.T  # can use transpose() instead of T
print(transpose)

# aggregation functions
#sum and mean
#sum of all elements
print(np.sum(arr))
#sum along columns
print(np.sum(arr,axis=0))
#sum along rows
print(np.sum(arr,axis=1))

#mean of all elements
print(np.mean(arr))
#mean of all elements along columns
print(np.mean(arr,axis=0))
#mean of all elements along rows
print(np.mean(arr,axis=1))

#minimum value
print(np.min(arr))
# maximum value
print(np.max(arr))
#index of minimum value
print(np.argmin(arr))
#index of maximum value
print(np.argmax(arr))
