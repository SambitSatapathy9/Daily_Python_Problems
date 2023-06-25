#Problem 2 (25.06.2023)
## Problem Statement - Write a Python program to print the Fibonacci series up to a given number.
num = int(input("Enter the length of Fibonacci series:"))
num1 = 0
num2 = 1
next_num = 0
count = 1

while (count <= num):
  print(next_num, end = ",")
  count += 1
  num1 = num2
  num2 = next_num
  next_num = num1 + num2
  t_number = num1 + num2
