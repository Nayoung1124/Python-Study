import numpy

n = input()
my_array = []
for i in range(int(n)):
    my_array.append(list(map(float, input().strip().split(' '))))
print(numpy.linalg.det(my_array))
