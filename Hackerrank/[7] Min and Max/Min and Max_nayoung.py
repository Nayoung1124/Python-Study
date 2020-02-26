import numpy


n, m = input().split()
my_array = []

for i in range(int(n)):
    my_array.append(list(map(int, input().strip().split(' '))))

a_min = numpy.min(my_array, axis = 1)
print(numpy.max(a_min, axis = 0))
