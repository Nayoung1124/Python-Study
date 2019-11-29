import numpy as np


arr = np.array(input().strip().split(), float)
x = float(input().strip())

print(np.polyval(arr, x))
