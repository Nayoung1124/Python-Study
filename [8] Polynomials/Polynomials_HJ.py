import numpy

arr = numpy.array(input().split(), float)
n = int(input())
print(numpy.polyval(arr, n))
