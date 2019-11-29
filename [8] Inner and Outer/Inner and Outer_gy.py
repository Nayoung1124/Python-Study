import numpy

arr_A = numpy.array(input().split(), int)
arr_B = numpy.array(input().split(), int)

print(numpy.inner(arr_A,arr_B))
print(numpy.outer(arr_A,arr_B))

