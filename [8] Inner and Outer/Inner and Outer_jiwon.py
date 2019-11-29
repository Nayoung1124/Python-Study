import numpy as np

A = np.array(input().strip().split(), int)
B = np.array(input().strip().split(), int)

print(np.inner(A,B))
print(np.outer(A,B))
