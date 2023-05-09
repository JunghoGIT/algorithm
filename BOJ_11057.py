N = int(input())

base = [0 for _ in range(10)]
dp = [base] * N
dp[0] = [1 for _ in range(10)]

for i in range(1, len(dp)):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])

print(sum(dp[N-1]) % 10007)