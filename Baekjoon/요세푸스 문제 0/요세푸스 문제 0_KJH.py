# 요세푸스 0
from collections import deque as dq

n, k = map(int, input().split())
circle = dq([i for i in range(1, n + 1)])
result=[]

while circle:
    for i in range(k - 1):
        circle.append(circle[0])
        circle.popleft()
    result.append(circle.popleft())

print("<", end="")
print(*result, sep=", ", end="")
print(">")
