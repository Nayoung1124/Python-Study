import numpy
N = int(input())

A = []
B = []
for x in range(N):
    A.append(list(map(int,input().split())))
    
for x in range(N):
    B.append(list(map(int,input().split())))

print (numpy.dot(A,B))
