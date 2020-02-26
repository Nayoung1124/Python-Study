import numpy
numpy.set_printoptions(sign=' ')
a=[]
a.append(list(map(float, input().strip().split(' '))))
arr = numpy.array(a)

print(numpy.floor(arr)[0])
print(numpy.ceil(arr)[0])
print(numpy.rint(arr)[0])

