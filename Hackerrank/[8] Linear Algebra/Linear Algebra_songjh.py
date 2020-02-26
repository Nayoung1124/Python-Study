import numpy as np

N = int(input())

list_ = []

for _ in range (N):
    A = input().strip().split()
    list_.append(A)
array_ = np.array(list_, float)

res = np.linalg.det(array_)

print (round(res, 2))
