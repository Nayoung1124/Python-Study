47/90 fail
-----------
def first(t,S): #append
    t_2nd=t.pop()
    t_string=list(t_2nd) # ['a', 'b', 'c']
    S.append(t_string)
    return S

def second(t,S): #delete
    t_2nd=t.pop()
    t_number=int(t_2nd)
    S.pop(t_number-1)

    return S

def thrid(t,S): #print
    pass #t_number=int(t_2nd)


def fourth(t,S): #undo
    pass

q=int(input())
t=list(input().rstrip().split()) #print(t)=['1', 'abc']
S=[]
#for i in range(q):
if t[0]=='1':
    a = first(t,S)
    print(a)
elif t[0]=='2':
    b = second(t,S)
    print(b)
elif t[0]=='3':
    c = third(t,S)
    print(c)
else :
    d = fourth(t,S)
    print(d)
