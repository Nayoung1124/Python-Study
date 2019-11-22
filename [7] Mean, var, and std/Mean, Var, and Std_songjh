import numpy

num = input().strip().split() 
arr = numpy.array(num, int) # [N,M]
list_ = []

for _ in range (arr[0]):
    A = input().strip().split()
    list_.append(A)
array_ = numpy.array(list_, int)
numpy.set_printoptions(sign=' ')

print (numpy.mean(array_, axis = 1))
print (numpy.var(array_, axis = 0))

std_ = numpy.std(array_, axis = None)
print (round(std_, 11)) # 소수점을 11번째 자리까지만 나타낸다.
