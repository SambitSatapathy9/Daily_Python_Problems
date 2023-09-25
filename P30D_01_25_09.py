#DAY 01 - 25.09.2023
#Q1 - Transpose Matrix using Python
import numpy as np
def transpose(matrix):
    
    # Create a matrix
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    
    # Transpose the matrix
    transposed_matrix = np.transpose(matrix)  # or matrix.T
    
    # Print the matrices
    print("Original Matrix:")
    print(matrix)
    
    print("\nTransposed Matrix:")
    print(transposed_matrix)

