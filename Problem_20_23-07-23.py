#Problem 20 (23-07-2023)
#Problem Statement: Write a python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))
array_2d = [[0 for j in range(col)] for i in range(row)]

for m in range(row):
    for n in range(col):
        product[m][n] = m*n

print(array_2d)
