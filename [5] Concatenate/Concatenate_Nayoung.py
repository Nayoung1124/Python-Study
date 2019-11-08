import numpy

n, m, p = input().split()
N = []
M = []
for i in range(int(n)):
    N.append(list(map(int, input().strip().split(' '))))

for i in range(int(m)):
    M.append(list(map(int, input().strip().split(' '))))

NN = numpy.array(N)
MM = numpy.array(M)

print (numpy.concatenate((NN, MM), axis = 0))


