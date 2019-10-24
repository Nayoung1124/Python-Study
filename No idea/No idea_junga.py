n , m = list(map(int, input().split()))
n = list(map(int, input().split()))
m_A = set(map(int, input().split()))#중복요소 없애기 위해 list 대신 set사용
m_B = set(map(int, input().split()))

H = 0

for i in n:
    if i in m_A:
        H += 1
    elif i in m_B:
        H -= 1
print(H)
