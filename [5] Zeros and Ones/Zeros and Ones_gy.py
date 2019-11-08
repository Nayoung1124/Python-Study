import numpy as np

size = input().split()


arr = np.array(size, int)


print (np.zeros(arr, dtype = np.int))
print (np.ones(arr, dtype = np.int))
