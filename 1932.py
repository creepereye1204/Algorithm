import copy
n = int(input())


semo = [list(map(int, input().split(" "))) for _ in range(n)]
dp = copy.deepcopy(semo)

dp[0] = semo[0]

for i in range(1, n):
    for j in range(i + 1):

        if j < i:
            right = dp[i - 1][j]
        else:
            right = 0
        if 0 < j:
            left = dp[i - 1][j - 1]
        else:
            left = 0
        dp[i][j] = max(left, right) + semo[i][j]
print(max(dp[-1]))
