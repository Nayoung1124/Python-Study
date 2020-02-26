import numpy
numpy.set_printoptions(sign=' ')

n, m = [int(i) for i in input().split()]
a = numpy.eye(n, m)
print(a)
