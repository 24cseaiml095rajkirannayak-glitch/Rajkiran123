# 1.WAP for ndarray Object, Indexing, and Slicing. 

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", arr)
arr = np.array([[10, 20, 30], [40, 50, 60]])
print("Element at (0, 1):", arr[0, 1]) # Indexing
print("Row 1:", arr[1, :]) # Slicing rows
print("Column 2:", arr[:, 2]) # Slicing columns