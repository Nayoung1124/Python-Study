import numpy

numpy.set_printoptions(sign=' ') 

N, M, P = list(map(int, input().strip().split()))

# create numpy arrays
arr_1, arr_2 = [], []
for i in range(N):
    arr_1.append(input().strip().split())

for i in range(M):
    arr_2.append(input().strip().split())

np_arr_1 = numpy.array(arr_1, int)
np_arr_2 = numpy.array(arr_2, int)

# concatenate
print(numpy.concatenate((np_arr_1, np_arr_2), axis = 0) )
