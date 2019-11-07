import numpy

a=input().strip().split(' ') # ['2', '2']
b=[]
a_=int(a.pop(0))

for i in range(a_): #2
    c=input().strip().split(' ')
    b.append(c)
    arr=numpy.array(b,int)
 
print(numpy.transpose(arr))
print(arr.flatten())
