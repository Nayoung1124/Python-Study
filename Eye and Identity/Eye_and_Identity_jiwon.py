import numpy

numpy.set_printoptions(sign=' ') 

N, M = list(map(int, input().strip().split()))

print(numpy.eye(N, M))
