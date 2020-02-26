import numpy

NM=input().split()
N=int(NM[0])
M=int(NM[1])
a=[]

for i in range(N):
    a.append(list(map(int, input().strip().split(' '))))

A=numpy.array(a)
b=numpy.sum(A,axis=0)
print(numpy.prod(b))
