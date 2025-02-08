#Extract an element in the matrix.
import numpy as np

matrix = np.array([[10, 20, 30, 40, 50],
                   [60, 70, 80, 90, 100],
                   [110, 120, 130, 140, 150],
                   [160, 170, 180, 190, 200],
                   [210, 220, 230, 240, 250]])

element = matrix[2, 3]
print("Extracted Element:", element)
