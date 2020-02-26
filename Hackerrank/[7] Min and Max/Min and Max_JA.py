import numpy

N,M = map(int,input().split())

A = []

for _ in range(N):
    A.append(list(map(int,input().split())))

arr = numpy.array(A)

arr_min = numpy.min(arr,axis = 1)
print(numpy.max(arr_min,axis = 0))
