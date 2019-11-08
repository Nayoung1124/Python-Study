import numpy

numpy.set_printoptions(sign=' ') 

D = tuple(map(int, input().strip().split()))

print( numpy.zeros(D, dtype = numpy.int) )
print( numpy.ones(D, dtype = numpy.int) )
