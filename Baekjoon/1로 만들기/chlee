import sys

# 입력 받기
N = int(sys.stdin.readline())

# dp 리스트 정의
dp = [0 for _ in range(N+1)]

# dp에 오름차순으로 채우기.
# dp[n]의 값이 의미하는 것은 주어진 세개의 연산을 이용하여 n의 숫자를 만들어 낼 수 있는 최소의 연산 개수
for i in range(1, len(dp)):
    if i+1 < len(dp) and (dp[i+1] is 0 or dp[i+1] > dp[i]+1):
        dp[i+1] = dp[i] + 1
    if 2*i < len(dp) and (dp[2*i] is 0 or dp[2*i] > dp[i]+1):
        dp[2*i] = dp[i] + 1
    if 3*i < len(dp) and (dp[3*i] is 0 or dp[3*i] > dp[i]+1):
        dp[3*i] = dp[i] + 1

print(dp[-1])
