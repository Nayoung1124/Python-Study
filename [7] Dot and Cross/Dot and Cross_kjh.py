import numpy

N=int(input())
a=[]
b=[]

for i in range(N):
    a.append(list(map(int, input().strip().split(' '))))

for i in range(N):
    b.append(list(map(int, input().strip().split(' '))))

aa=numpy.array(a)
bb=numpy.array(b)

print(numpy.dot(aa,bb))
