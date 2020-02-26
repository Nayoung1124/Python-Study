import numpy

A = input().strip().split() 
arr = numpy.array(A, int)

numpy.set_printoptions(sign=' ')

print (numpy.eye(arr[0], arr[1], k = 0))
