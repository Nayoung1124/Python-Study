import numpy

mnp=input().split()
m=int(mnp[0])
n=int(mnp[1])
p=int(mnp[2])
f=[]
g=[]

for i in range(m): #0~3
    a=input().split()
    f.append(a)
    arr1=numpy.array(f,int)

for j in range(m,n+m):
    a=input().split()
    g.append(a)
    arr2=numpy.array(g,int)
    

print (numpy.concatenate((arr1,arr2),axis=0))
