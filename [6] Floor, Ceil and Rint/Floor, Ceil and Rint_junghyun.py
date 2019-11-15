import numpy

arr = input().strip().split() 
array = numpy.array(arr, float)
numpy.set_printoptions(sign=' ')

print (numpy.floor(array))
print (numpy.ceil(array))
print (numpy.rint(array))
