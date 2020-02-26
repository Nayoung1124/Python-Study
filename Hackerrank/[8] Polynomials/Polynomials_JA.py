import numpy
n = list(map(float,input().split()))
m = int(input())
print(numpy.polyval(n,m))
