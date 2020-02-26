import numpy 

A=list(map(int,input().split()))
B=list(map(int,input().split()))

A_=numpy.array(A)
B_=numpy.array(B)

print(numpy.inner(A,B))
print(numpy.outer(A,B))
