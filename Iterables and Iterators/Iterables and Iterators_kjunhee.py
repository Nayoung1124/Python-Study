from itertools import combinations
import math

n=int(input())

items= list(input().rstrip().split())

k=int(input())

comb=list(combinations(items,k))
num_comb=len(comb)
num_a=0
#print(comb)
for i in comb:
    p = 'a' in i
    if p==1:
        num_a=num_a+1
    


print(round(num_a/num_comb,12))
