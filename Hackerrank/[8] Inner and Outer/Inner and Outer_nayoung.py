import numpy

arr1 = list(map(int, input().rstrip().split()))
arr2 = list(map(int, input().rstrip().split()))

print(numpy.inner(arr1,arr2))
print(numpy.outer(arr1,arr2))
