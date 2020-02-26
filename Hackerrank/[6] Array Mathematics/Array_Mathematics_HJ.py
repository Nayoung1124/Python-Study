import numpy

n, m = [int(i) for i in input().split()]

A = []
B = []

for i in range(n):
    A.append([int(j) for j in input().split()])

for i in range(n):
    B.append([int(j) for j in input().split()])

A = numpy.array(A)
B = numpy.array(B)

print(A+B, A-B, A*B, A//B, A%B, A**B, sep='\n')
