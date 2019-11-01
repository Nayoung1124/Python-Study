import numpy



a, b = input().split()
arr = [[i for i in input().split()] for j in range(int(a))]
arr = numpy.array(arr, int)
print(numpy.transpose(arr), arr.flatten(), sep='\n')
