import itertools

N = int(input())
N_ilst = list(input().rstrip().split())
K = int(input()) 

check_list = list(itertools.combinations(N_ilst, K)) # N_list의 모든 조합 : nCk
a_check = [] # a가 들어있을 list

for i in check_list:
    if 'a' in i:
        a_check.append(i)

num1 = len(a_check)
num2 = len(check_list)
out = num1/num2

print(out)
