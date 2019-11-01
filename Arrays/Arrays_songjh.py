import numpy

def arrays(arr):
    A = numpy.array(arr[::-1], float)
    return A

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
