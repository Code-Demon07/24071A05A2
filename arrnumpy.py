#Stack two NumPy arrays vertically and horizontally.
import numpy as np


array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])


vertical_stack = np.vstack((array1, array2))
print("Vertical Stack:\n", vertical_stack)


horizontal_stack = np.hstack((array1, array2))
print("Horizontal Stack:\n", horizontal_stack)
