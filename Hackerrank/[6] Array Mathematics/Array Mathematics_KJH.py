import numpy
import math

NM=input().split()
N=int(NM[0])
M=int(NM[1])
a=[]
b=[]


for i in range(N):
    a.append(list(map(int, input().strip().split(' '))))
for i in range(N):
    b.append(list(map(int, input().strip().split(' '))))

A=numpy.array(a)
B=numpy.array(b)

print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
#c=numpy.round(numpy.divide(A,B),0)
print(A//B)
print(numpy.mod(A,B))
print(numpy.power(A,B))
