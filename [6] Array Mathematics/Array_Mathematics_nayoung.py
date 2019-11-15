import numpy

n, m = input().split()
a, b = [], []
for i in range(int(n)):
    a.append(list(map(int, input().strip().split(' '))))
for i in range(int(n)):
    b.append(list(map(int, input().strip().split(' '))))
a=numpy.array(a)
b=numpy.array(b)

print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
c = numpy.divide(a,b)
c = numpy.array(c,int)
print(c)
print(numpy.mod(a,b))
print(numpy.power(a,b))