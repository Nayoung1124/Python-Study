import numpy
numpy.set_printoptions(legacy='1.13')
N,M =  map(int,input().split())

A = []
for _ in range(N):
    A.append(list(map(int,input().split())))


arr = numpy.array(A)


print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(numpy.std(arr))

