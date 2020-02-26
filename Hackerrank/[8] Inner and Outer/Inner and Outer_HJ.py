import numpy

arr = numpy.array([i for i in input().split()], int)
arr2 = numpy.array([i for i in input().split()], int)
print(numpy.inner(arr, arr2))
print(numpy.outer(arr, arr2))
