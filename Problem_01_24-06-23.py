#Problem 1 (24.06.2023)
## Problem Statement - Write a Python program to calculate the factorial of a given number.
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

num = int(input("Enter a number: "))
fact = factorial(num)
print(f"The factorial of {num} is {fact}")
