import numpy


N,M = map(int, input().split())

#A = numpy.array([list(map(int, input().strip().split(' ')))])

#B = numpy.array([list(map(int, input().strip().split(' ')))])

A=[]
B=[]
for i in range(N):
    S = list(map(int, input().strip().split(' ')))
    A.append(S)
for i in range(N):
    S = list(map(int, input().strip().split(' ')))
    B.append(S)

A = numpy.array(A)
B = numpy.array(B)

print(numpy.add(A,B), numpy.subtract(A,B), numpy.multiply(A,B), numpy.floor_divide(A,B), numpy.mod(A,B), numpy.power(A,B), sep = '\n')
