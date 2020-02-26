import math
from copy import copy as copy

n = int(input())
realn = copy(n)
ans = 0
 
while True:
    if n ==1:
        break
    elif n%3 == 0:
        n= n//3
        ans += 1
    elif n%3 == 1:
        n -= 1
        ans +=1
    elif n%3 == 2:
        if n%2 ==0:
            n = n//2
            ans += 1
        else:
            n -=2
            ans+=2
if realn==1: print(1)
else: print(ans)
