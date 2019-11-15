import numpy
numpy.set_printoptions(sign=' ')


A = [i for i in input().split()]
A = numpy.array(A, float)
print(numpy.floor(A), numpy.ceil(A), numpy.rint(A), sep='\n')
