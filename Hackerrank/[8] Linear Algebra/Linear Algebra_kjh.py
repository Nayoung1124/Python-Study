import numpy
numpy.set_printoptions(legacy='1.13')

N=int(input())
A=[]
for i in range(N):
    A.append(list(map(float, input().strip().split(' '))))

print(numpy.linalg.det(A))
