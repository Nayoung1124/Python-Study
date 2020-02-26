N = int(input())
dp = [0]*(N+1) #미리 dp에 저장공간을 만들어줍니다.

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 #1뺴고 최소연산
    if i%2 == 0 : # 2로 누어 떨어질 경우
        if dp[i] > dp[i//2] + 1: #비교 후 저장
            dp[i] = dp[i//2] + 1
    if i%3 == 0: # 3으로 나누어 떨어질 경우
        if dp[i] > dp[i//3] + 1: #비교 후 저장
            dp[i] = dp[i//3] + 1

print(dp[N])
