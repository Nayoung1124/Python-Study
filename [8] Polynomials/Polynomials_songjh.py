import numpy as np

A = np.array(input().split(), float)
num = int(input())

print (np.polyval(A, num))
