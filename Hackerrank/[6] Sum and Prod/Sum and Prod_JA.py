import numpy

N, M = list(map(int, input().strip().split()))
list_=[]

for i in range(N):
    S=list(map(int, input().strip().split(' ')))   
    list_.append(S)
    
list_arr = numpy.array(list_)

sum_arr = numpy.sum(list_arr,axis=0)
prod_arr = numpy.prod(sum_arr)
print(prod_arr)
      
      
