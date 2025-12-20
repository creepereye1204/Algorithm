N = int(input())
arr = [0]*367

for _ in range(N):
    S, E = map(int, input().split())
    for i in range(S, E+1):
        arr[i] += 1

ans = mx = s = 0
for i in range(367):
    if arr[i] != 0:
        s += 1
        mx = max(mx, arr[i])
    else:
        ans += s*mx
        s = mx = 0
print(ans)
