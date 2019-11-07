import numpy

A = input().strip().split() 
arr = numpy.array(A, int) # [2,2]
list_ = []

for _ in range (arr[0]):
    B = input().strip().split()
    list_.append(B)
    
array = numpy.array(list_, int)

print (numpy.transpose(array))
print (array.flatten())
