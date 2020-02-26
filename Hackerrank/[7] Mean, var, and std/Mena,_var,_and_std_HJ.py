import numpy

numpy.set_printoptions(legacy='1.13')

n, m = input().split()
arr = []

for i in range(int(n)):
    arr.append(input().split())

arr = numpy.array(arr, float)
print(arr.mean(axis=1), arr.var(axis=0), arr.std(), sep='\n')
