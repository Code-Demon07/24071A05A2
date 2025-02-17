import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

v_stack = np.vstack((a, b))
print("Vertical Stack:\n", v_stack)

h_stack = np.hstack((a, b))
print("Horizontal Stack:\n", h_stack)
