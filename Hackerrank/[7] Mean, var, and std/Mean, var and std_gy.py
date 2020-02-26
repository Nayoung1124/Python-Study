import numpy as np

np.set_printoptions(sign=' ') 

N, M = input().split()
N = int(N)
S = []

for _ in range(N):
    s = list(map(int, input().split()))
    S.append(s)
#print(S)
arr = np.array(S)
#print(arr)

print (np.mean(arr, axis = 1))

print (np.var(arr, axis = 0))

std_ = np.std(arr, axis = None)
ans = round(std_,12)
print (ans)
