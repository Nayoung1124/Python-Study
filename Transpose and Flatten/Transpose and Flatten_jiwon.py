import numpy

N, M = list(map(int, input().strip().split()))

arr = []
for i in range(N):
    arr.append(input().strip().split())

arr = numpy.array(arr, int)


print (numpy.transpose(arr))
print (arr.flatten())
