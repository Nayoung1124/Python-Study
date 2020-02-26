import numpy

numpy.set_printoptions(sign=' ') 

N, M = list(map(int, input().strip().split()))

arr = []
for i in range(N):
    arr.append(input().strip().split()) 
np_arr = numpy.array(arr, int)

# sum
sum_result = numpy.sum(np_arr, axis=0)

# product
prod_result = numpy.prod(sum_result)

print(prod_result)
