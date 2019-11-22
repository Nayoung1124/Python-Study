import numpy

n = int(input()) 
a, b, c = [], [], []

for i in range(n*2):
    a.append([int(j) for j in input().split()])

for k in range (n):
    b.append(a[k])
    c.append(a[-k])
print(numpy.dot(b,c))
