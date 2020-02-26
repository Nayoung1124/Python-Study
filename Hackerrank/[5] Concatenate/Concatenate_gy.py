import numpy

M, N, P = input().split()


arr = []
arr2 = []


for _ in range(int(M)):
    p = list(map(int, input().split()))
    arr.append(p)

array_1 = numpy.array(arr)

for _ in range(int(N)):
    p = list(map(int, input().split()))
    arr2.append(p)

array_2 = numpy.array(arr2)

ans = numpy.concatenate((array_1, array_2), axis = 0)   

print(ans)

