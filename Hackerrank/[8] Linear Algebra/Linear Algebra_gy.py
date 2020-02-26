import numpy
N = int(input())
S = []
for _ in range(N):
    s = numpy.array(input().split(), float)
    S.append(s)

ans = numpy.linalg.det(S)
print(round(ans,3))  


