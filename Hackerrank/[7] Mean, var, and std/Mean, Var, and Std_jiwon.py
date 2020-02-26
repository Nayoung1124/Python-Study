import numpy

# numpy.set_printoptions(sign=' ') 
numpy.set_printoptions(legacy='1.13')

N, M = list(map(int, input().strip().split()))

arr = [list(map(int, input().strip().split())) for _ in range(N)]
arr = numpy.array(arr)

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.std(arr))

