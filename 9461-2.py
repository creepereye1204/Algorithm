T = int(input())
dp = [0]*101
dp[:4] = [1, 1, 1, 2]
for i in range(3, 101):
    dp[i] = dp[i-2]+dp[i-3]
for _ in range(T):
    print(dp[int(input())-1])
