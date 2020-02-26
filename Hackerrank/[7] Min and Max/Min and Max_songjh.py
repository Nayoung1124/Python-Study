import numpy

num = input().strip().split() 
arr = numpy.array(num, int) # [N,M]
list_ = []

for _ in range (arr[0]):
    A = input().strip().split()
    list_.append(A)
array_ = numpy.array(list_, int)

min_ = numpy.min(array_, axis = 1)

print (numpy.max(min_))
