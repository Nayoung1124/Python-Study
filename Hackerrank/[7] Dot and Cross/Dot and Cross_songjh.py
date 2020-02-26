import numpy

num = input().strip().split() 
arr = numpy.array(num, int) # [N,M]
list_A = []
list_B = []

for _ in range (arr[0]):
    A = input().strip().split()
    list_A.append(A)
array_A = numpy.array(list_A, int)

for _ in range (arr[0]):
    B = input().strip().split()
    list_B.append(B)
array_B = numpy.array(list_B, int)

print (numpy.dot(array_A, array_B))
