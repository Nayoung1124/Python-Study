import numpy
numpy.set_printoptions(sign=' ')

NM=input().split()
N=int(NM[0])
M=int(NM[1])

print (numpy.eye(N,M, k = 0))
