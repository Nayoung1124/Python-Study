import numpy

P=list(map(float,input().split()))
x=float(input())
arr=numpy.array(P)
print(numpy.polyval(arr,x))
