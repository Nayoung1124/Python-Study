import numpy

A = input().strip().split() 
arr = numpy.array(A, int)

print (numpy.zeros(arr, dtype = numpy.int))
print (numpy.ones(arr, dtype = numpy.int))
