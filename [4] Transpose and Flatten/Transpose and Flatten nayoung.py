import numpy

n, m = input().split()
a = []
for i in range(int(n)):
    a.append(list(map(int, input().strip().split(' '))))


a = numpy.array(a)
b = numpy.transpose(a)
c = a.flatten()
print (b)
print (c)
