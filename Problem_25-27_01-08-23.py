#Problem 25 (01.08.2023)
## Problem Statement - Write a Python program to Create a 4x4 NumPy array with random floating-point numbers between 0 and 1. 
#Replace all values less than 0.5 with 0 and all values greater than or equal to 0.5 with 1.

import numpy as np

arr = np.random.rand(4,4)
print("Original Array: \n", arr)

arr[arr<0.5] = 0
arr[arr>=0.5]= 1

print("Modified Array: \n", arr)

#Problem 26 (01.08.2023)
## Problem Statement - Write a Python program to Create a 5x5 NumPy array with random integers between 1 and 100. 
#Find the minimum and maximum values in the entire array.

import numpy as np

arr = np.random.randint(1,101,size = (5,5))
print("Array:\n", arr)

#Minimum value of the array
min_arr = np.min(arr)
print(f"Minimum value in the array: {min_arr}")

#Maximum value of the array
max_arr = np.max(arr)
print(f"Maximum value in the array: {max_arr}")

#Problem 27 (01.08.2023)
## Problem Statement - Write a Python program to Create a 5x5 NumPy array with random integers between 1 and 100. 
#Find the minimum and maximum values of (1) each row (2) each column

import numpy as np

arr = np.random.randint(1,101,size = (5,5))
print("Array:\n", arr)

#Minimum value of the array in each row
min_arr = np.min(arr, axis = 1)
print(f"Minimum value in each row: {min_arr}")

#Maximum value of the array in each column
max_arr = np.max(arr, axis = 0)
print(f"Maximum value in each column: {max_arr}")

