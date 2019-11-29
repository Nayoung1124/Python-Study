import numpy as np

np.set_printoptions(legacy='1.13')

N = int(input().strip())
A = [input().strip().split() for _ in range(N)]
A = np.array(A, float)

print(np.linalg.det(A))



