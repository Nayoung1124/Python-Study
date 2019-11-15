import numpy

numpy.set_printoptions(sign=' ')

A_array = numpy.array(input().strip().split(), float)

print(numpy.floor(A_array))
print(numpy.ceil(A_array))
print(numpy.rint(A_array))
