import numpy as np

A = input().strip().split(' ')
arr = np.array(A, int) # 문자열 A를 numpy array int형으로 변환
print (np.reshape(arr,(3,3)))
