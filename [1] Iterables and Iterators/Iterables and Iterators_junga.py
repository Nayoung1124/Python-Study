from itertools import combinations

N = int(input())
K = list(input().rstrip().split())
D = int(input())

com = []
com1 = 0

com=list(combinations(K,D))
total = len(com)

for i in range(len(com)):
    if 'a' in com[i]:
        com1 += 1

    else :
        pass

print(com1/total)
