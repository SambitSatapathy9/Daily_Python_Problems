#Problem 12 (09-07-2023)
#Problem Statement: Write a python program to check whetherr a number is a perfect number or not
    #Note: A perfect number is a positive number is a positive integer that is equal to the sum of its 
    #proper positive divisors. Also, it is half the sum of all its positive divisors
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

m = int(input("Enter the number: "))
print(perfect_number(m))
    
