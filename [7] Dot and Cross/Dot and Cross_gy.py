import numpy

N = int(input())

count = 0
S_1 = []
S_2 = []

for _ in range(2*N):
    count+=1
    s = list(map(int, input().split()))
    if count < N+1 :
        S_1.append(s)

    if count > N : 
        S_2.append(s)

A = numpy.array(S_1)
B = numpy.array(S_2)

print (numpy.dot(A, B))
