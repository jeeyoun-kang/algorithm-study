import sys
input = sys.stdin.readline

dp = [[0] * 10 for i in range(1001)]

n = int(input())

for i in range(10): # 자리 수가 1인 경우
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0: #끝자리 0인경우는 1가지
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(sum(dp[n]) % 10007)