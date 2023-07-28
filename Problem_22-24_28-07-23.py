#Problem 22 (28.06.2023)
## Problem Statement - Write a Python program to Flatten a Matrix in Python using NumPy

import numpy as np
arr = np.array([[6, 9], [8, 5], [18, 21]])
arr.flatten()             # using array.flatten() method

##Problem 23 Statement  -  Write a Python Program to create a 3x3 NumPy array with random integers between 1 and 20. 
#Calculate the sum and mean of the array.

import numpy as np
arr = np.random.randint(1,21,size=(3,3))
print("Array")
print(arr)

sum_arr = np.sum(arr)
mean_arr = np.mean(arr)
print("Sum of array:", sum_arr)
print("Mean of array:", mean_arr)

# Problem 24: Create a NumPy array of numbers from 1 to 100. Reshape the array into a 10x10 matrix. 
#Calculate the sum of each row and each column.

import numpy as np
arr = np.arange(1,101,1)
arr = arr.reshape(10,10)
sum_arr_row = np.sum(arr, axis = 1)
sum_arr_column = np.sum(arr, axis = 0)
