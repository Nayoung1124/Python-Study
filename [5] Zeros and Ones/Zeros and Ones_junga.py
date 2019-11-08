import numpy


a,b,c = map(int,input().strip().split())

print(numpy.zero((a,a),dtype = numpy.int))
print(numpy.ones((a,a),dtype = numpy.int))
