import numpy

numpy.set_printoptions(sign=' ')
A=list(map(float, input().strip().split(' ')))

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
