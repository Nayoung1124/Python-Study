n , m = list(map(int, input().split()))
n1 = list(map(int, input().split()))

# 중복된 경우도 한번만 카운트 해야하므로중복을 없애기위해 set을 사용
A = set(map(int, input().split()))
B = set(map(int, input().split()))

A_check = [] # n리스트와 A집합의 공통인수를 모아둔 리스트
B_check = [] # n리스트와 B집합의 공통인수를 모아둔 리스트

for i in n:
    if i in A:
        A_check.append(i)     
    elif i in B:
        B_check.append(i)

num1 = len(A_check) 
num2 = len(B_check)
out = num1-num2

print(out)
