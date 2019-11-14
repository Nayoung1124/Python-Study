import numpy


N, M = list(map(int, input().strip().split()))

A, B = [], []
for i in range(N):
    A.append(input().strip().split())

for i in range(N):
    B.append(input().strip().split())

a = numpy.array(A, int)
b = numpy.array(B, int)

print(numpy.add(a, b))

print(numpy.subtract(a, b))

print(numpy.multiply(a, b))

print(a//b)

print(numpy.mod(a, b)) 

print(numpy.power(a, b)) 
