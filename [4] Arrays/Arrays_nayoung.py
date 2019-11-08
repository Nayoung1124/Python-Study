import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.array(arr, float)
    a = a[::-1]
    return a
arr = input().strip().split(' ')