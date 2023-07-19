#Problem 18 (19-07-2023)
#Problem Statement: Write a python program to multiply two matrices
""" 
Input : X = [[1, 7, 3],
             [3, 5, 6],
             [6, 8, 9]]
       Y = [[1, 1, 1, 2],
           [6, 7, 3, 0],
           [4, 5, 9, 1]]
"""
# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix   
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]


for i in range(len(A)):                            #Iterating by the row A
      for j in range(len(B)[0]):                  #Iterating by the column of B
            for k in range(len(B)):              #Iterating by the rows of B
                  result[i][j] = A[i][k] * B[k][j]


for r in result
    print(r)
