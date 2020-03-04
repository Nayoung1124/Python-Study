N = int(input())
dp = [[0 for j in range(10)] for i in range(N)]
dp[0] = [0]+[1]*9
for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
            continue
        if j == 9:
            dp[i][j] = dp[i-1][8]
            continue
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[-1])%1000000000)
