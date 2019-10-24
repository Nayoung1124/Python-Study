

from itertools import combinations


def check(array):
    count = 0
    for i in array:
        if 'a' in i:
            count += 1
        else:
            pass
    return count

size = input().split()

U = list(input().split())

k = int(input())

w_size = 0

whole = list(combinations(U,k))

'''
p = list()
for i in range(len(U)): # 0
    for j in range(i+1,len(U)): # 1
        d = list([U[i],U[j]]) 
        #print(d)
        p.append(d)
#print(p)
'''
#print(whole)

ans = check(whole)

n = ans/len(whole)
ans = round(n,12)

print(ans)



