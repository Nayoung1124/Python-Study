import sys
from collections import deque

# 입력 받기
N, K = map(int, sys.stdin.readline().split(" "))

# 1 ~ N 까지의 수가 들어있는 큐 선언
q = deque(list(range(1, N+1)))

# 제거되는 숫자를 담을 result 리스트 선언
result = []

# 큐에 한 사람이 남을 때까지 반복
while len(q) != 1:
    # K-1 번은 살려서 큐의 맨 뒤로 보내고
    for _ in range(K-1):
        q.append(q.popleft())
    # K번 째는 제거(result에 담아줌.)
    result.append(q.popleft())
# 마지막 사람을 마저 추가해주고,
result.append(q.popleft())
# 출력 형태로 맞춰줌.
result_str = "<"+', '.join(str(e) for e in result)+">"

print(result_str)
