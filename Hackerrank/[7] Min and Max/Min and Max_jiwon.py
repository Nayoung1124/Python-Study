import numpy

N, M = list(map(int, input().strip().split()))

arr = [list(map(int, input().strip().split())) for _ in range(N)]
arr = numpy.array(arr)

arr = numpy.min(arr, axis=1)
result = numpy.max(arr, axis=0)

print(result)
