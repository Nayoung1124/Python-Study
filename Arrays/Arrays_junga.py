import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr_ = numpy.array(arr, float)[::-1]#내림차순정렬

   
    return arr_

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
