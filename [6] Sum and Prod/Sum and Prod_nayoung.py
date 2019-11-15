import numpy

n, m = input().split()
a = []
for i in range(int(n)):
    a.append(list(map(int, input().strip().split(' '))))

ans_1 = numpy.sum(a, axis = 0)
ans_2 = numpy.prod(ans_1, axis = 0)
print(ans_2)