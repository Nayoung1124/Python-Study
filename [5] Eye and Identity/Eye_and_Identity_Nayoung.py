import numpy
numpy.set_printoptions(sign=' ')

n, m = input().split()

print(numpy.eye(int(n), int(m), k = 0))
