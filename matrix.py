#Use NumPy to perform basic matrix operations.
import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix addition
addition = A + B
print("Matrix Addition:\n", addition)

# Matrix subtraction
subtraction = A - B
print("\nMatrix Subtraction:\n", subtraction)

# Element-wise multiplication
elementwise_multiplication = A * B
print("\nElement-wise Multiplication:\n", elementwise_multiplication)

# Matrix multiplication
matrix_multiplication = np.dot(A, B)
print("\nMatrix Multiplication:\n", matrix_multiplication)

# Transpose of a matrix
transpose_A = A.T
print("\nTranspose of Matrix A:\n", transpose_A)

# Determinant of a matrix
determinant_A = np.linalg.det(A)
print("\nDeterminant of Matrix A:\n", determinant_A)

# Inverse of a matrix
inverse_A = np.linalg.inv(A)
print("\nInverse of Matrix A:\n", inverse_A)
