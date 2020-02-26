import sys
X = int(sys.stdin.readline())
dp = [0,0,1,1]
 
for i in range(4, X+1):
    dp.append(dp[i-1] + 1) # dp[i]를 우선 append해준다. 이때 i는 i-1보다 1만큼 숫자가 커진 것이므로 dp[i]는 dp[i-1]에서 단순히 1을 빼는 연산이 추가 된다는 가정으로 dp[i-1]에서 연산 횟수 한번을 추가로 더한 (dp[i-1] + 1)을 dp[i]에 저장하는 것이다.
 
    if i % 2 == 0: # i가 2로 나누어 떨어지면 
        ex = dp[i//2] + 1 # i//2로 나눈 인덱스의 요소 수(연산 수)에다가 처음 2로 나눈 연산 1번을 추가한 것을 ex라 한다.
        
        if dp[i] > ex:
            # 최소한의 연산 수를 구해야 하므로 ex가 처음 저장한 dp[i]의 값보다 작을 경우 dp[i] 를 ex로 업데이트 한다.
            dp[i] = ex
 
    if i % 3 == 0: # i가 3으로 나누어 떨어지면
        ex = dp[i//3] + 1 # i//3으로 나눈 인덱스의 요소 수(연산 수)에다가 처음 3로 나눈 연산 1번을 추가한 것을 ex라 한다.

        if dp[i] > ex:
            # 최소한의 연산 수를 구해야 하므로 ex가 처음 저장한 dp[i]의 값보다 작을 경우 dp[i] 를 ex로 업데이트 한다.
            dp[i] = ex

print(dp[X]) # 연산 수 출력
