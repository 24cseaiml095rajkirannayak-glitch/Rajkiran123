# 5.WAP for Saving and Loading Arrays. 

import numpy as np

arr = np.array([1, 2, 3, 4])
np.save('my_array', arr) # Save array
loaded_arr = np.load('my_array.npy') # Load array
print("Loaded array:", loaded_arr)