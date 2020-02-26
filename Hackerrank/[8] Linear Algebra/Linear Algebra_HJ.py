import numpy

n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())

arr = numpy.array(arr, float)

print(numpy.round_(numpy.linalg.det(arr), 2))
