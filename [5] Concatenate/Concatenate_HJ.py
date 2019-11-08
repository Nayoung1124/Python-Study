import numpy

def array(n):
    arr = []
    for i in range(int(n)):
        arr.append(input().split())

    return numpy.array(arr, int)

n, m, p = input().split()

arr_1 = array(n)
arr_2 = array(m)
print(numpy.concatenate((arr_1, arr_2), axis=0))

