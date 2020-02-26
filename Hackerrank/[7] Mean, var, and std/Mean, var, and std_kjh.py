import numpy
numpy.set_printoptions(sign=' ')

NM=input().split()
N=int(NM[0])
M=int(NM[1])
a=[]

for i in range(N):
    a.append(list(map(int, input().strip().split(' '))))

aa=numpy.array(a)
print(numpy.mean(aa, axis=1))
print(numpy.var(aa, axis=0))
print(numpy.round_(numpy.std(aa,axis=None),12))
