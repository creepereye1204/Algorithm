def solution(info, n, m):
    L = len(info)
    INF = float('inf')

    dp = [[INF] * (m) for _ in range(L+1)]
    dp[0][0] = 0

    for i in range(L):
        a, b = info[i]
        for j in range(m):
            if dp[i][j] == INF:
                continue

            if dp[i][j]+a < n:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+a)

            if j+b < m:
                dp[i+1][j+b] = min(dp[i+1][j+b], dp[i][j])

    ans = min(dp[L])
    return -1 if ans == INF else ans
