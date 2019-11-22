import numpy

n = int(input())

arr_a = []
arr_b = []

for i in range(n):
    arr_a.append(input().split())

for i in range(n):
    arr_b.append(input().split())

arr_a = numpy.array(arr_a, int)
arr_b = numpy.array(arr_b, int)

print(numpy.dot(arr_a, arr_b))
