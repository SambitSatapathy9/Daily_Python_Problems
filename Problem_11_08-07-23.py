#Problem 11 (08.07.2023)
## Problem Statement - Write a Python program to draw a simple pyramid pattern

#APPROACH 1 (Using for loop)
def pyramid(n):
    for i in range(n): # outer loop to handle number of rows                      # n in this case
        for j in range(0,i+1): # inner loop to handle number of columns           # values changing acc. to outer loop
            print("*",end = "") #printing stars
        print("\r")         # ending line after each row
      
n = 5
pyramid(5) #Execution of the program

#APPROACH 2 (Using recursion)
def pyramid(n):
    if n == 0:
        return:
    else:
      pyramid(n-1)
      print("*"*n)

n = 5
pyramid(n)
