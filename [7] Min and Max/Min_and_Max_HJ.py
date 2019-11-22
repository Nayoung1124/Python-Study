import numpy



n, m = input().split()
arr = []
for i in range(int(n)):
    arr.append(input().split())

arr = numpy.array(arr, int)
arr = numpy.min(arr, axis=1)
print(numpy.max(arr))
