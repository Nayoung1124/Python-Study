import numpy

A = input().strip().split() 
arr = numpy.array(A, int)
list_1 = []
list_2 = []

for _ in range (arr[0]-1):
    B = input().strip().split()
    list_1.append(B)

for arr[0] in range (arr[1]+1):
    C = input().strip().split()
    list_2.append(C)

array_1 = numpy.array(list_1, int)
array_2 = numpy.array(list_2, int)

print (numpy.concatenate((array_1, array_2), axis = 0))
