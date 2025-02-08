#Find unique elements in a NumPy array.
import numpy as np


array = np.array([1, 2, 2, 3, 4, 4, 4, 5, 6, 6])


unique_elements = np.unique(array)
print("Unique elements:", unique_elements)
