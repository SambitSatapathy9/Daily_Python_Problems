#Problem 8 (27.06.2023)
## Problem Statement - Write a Python program to create a histogram from a given list of integers
def histogram(items):
    for n in items:
        output = ''
        while n>0:
            output+= '*'
            n = n-1
        print(f"{output}")
       
histogram([2,3,16,7,8])
