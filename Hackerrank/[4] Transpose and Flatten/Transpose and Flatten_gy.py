import numpy


a = list(map(int,input().split()))
N = a[1]
p = []
for i in range(N):
    t = list(map(int,input().split()))
    p.append(t)

ans = numpy.array(p)

print(numpy.transpose(ans))
print(ans.flatten())

