import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)

print(numpy.inner(A,B))
print(numpy.outer(A,B))
