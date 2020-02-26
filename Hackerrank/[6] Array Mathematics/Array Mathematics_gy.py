import numpy

some = list(map(int, input().split()))

A = []
B = []

for _ in range(some[0]):
    a = numpy.array(input().split(),int)
    A.append(a)

for _ in range(some[0]):
    b = numpy.array(input().split(),int)
    B.append(b)



ans1 = numpy.add(A,B)
ans2 = numpy.subtract(A,B)
ans3 = numpy.multiply(A,B)
ans4 = numpy.divide(A,B) # dtype=int 왜 안되는거지...
ans4 = numpy.array(ans4,int)
ans5 = numpy.mod(A,B)
ans6 = numpy.power(A,B)



print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
print(ans6)


