import numpy

ans = input().split()
# print (ans)

if len(ans) == 4:
    n = ans[0]
    m = ans[1]
    l = ans[2]
    k = ans[3]
    print(numpy.zeros((int(n), int(m), int(l), int(k)), dtype=numpy.int))
    print(numpy.ones((int(n), int(m), int(l), int(k)), dtype=numpy.int))

if len(ans) == 3:
    n = ans[0]
    m = ans[1]
    l = ans[2]
    print(numpy.zeros((int(n), int(m), int(l)), dtype=numpy.int))
    print(numpy.ones((int(n), int(m), int(l)), dtype=numpy.int))

elif len(ans) == 2:
    n = ans[0]
    m = ans[1]
    l = 0
    print(numpy.zeros((int(n), int(m)), dtype=numpy.int))
    print(numpy.ones((int(n), int(m)), dtype=numpy.int))



