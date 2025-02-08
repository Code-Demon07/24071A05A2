#Generate a random number matrix of size 5*5 using NumPy.
import numpy as np

random_matrix = np.random.rand(5, 5)
print("Random Matrix (Uniform Distribution):\n", random_matrix)

random_int_matrix = np.random.randint(1, 101, size=(5, 5))
print("Random Integer Matrix:\n", random_int_matrix)

random_normal_matrix = np.random.randn(5, 5)
print("Random Matrix (Normal Distribution):\n", random_normal_matrix)

random_uniform_matrix = np.random.uniform(-10, 10, size=(5, 5))
print("Random Matrix (Custom Range):\n", random_uniform_matrix)
