import numpy

q = list(map(float, input().rstrip().split()))
a = int(input())
print(numpy.polyval(q,a))
