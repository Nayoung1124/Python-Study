import numpy as np

a,_ = input().split()
a = int(a)

nn = []

for _ in range(a):
    mm = np.array(input().split(),int)
    nn.append(mm)
s = np.sum(nn,axis = 0)
m = np.prod(s)
print(m)



