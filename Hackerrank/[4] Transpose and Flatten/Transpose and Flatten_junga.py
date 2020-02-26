import numpy

n, m = map(int, input().split())
myarr = []
for _ in range(n):
    a =  list(map(int,input().split()))
    myarr.append(a)

myarr = numpy.array(myarr)
print(numpy.transpose(myarr))
print(myarr.flatten())
