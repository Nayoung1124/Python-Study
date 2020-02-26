import numpy
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(float, input().split())))

result = numpy.linalg.det(a)
print (result.round(2))
