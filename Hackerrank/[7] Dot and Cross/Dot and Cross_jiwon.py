import numpy

N = int(input().strip())

A = [list(map(int, input().strip().split())) for _ in range(N)]
B = [list(map(int, input().strip().split())) for _ in range(N)]

A = numpy.array(A)
B = numpy.array(B)

print(numpy.dot(A, B))
