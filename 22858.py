import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p = list(map(int, input().split()))
d = list(map(lambda x: int(x)-1, input().split()))

ans = [0] * n
visited = [False] * n

for start in range(n):
    if visited[start]:
        continue

    # 사이클 찾기
    cycle = []
    cur = start
    while not visited[cur]:
        visited[cur] = True
        cycle.append(cur)
        cur = d[cur]

    L = len(cycle)
    shift = k % L

    # 사이클 내에서 K번 이동한 위치로 값 배치
    for i in range(L):
        ans[cycle[(i + shift) % L]] = p[cycle[i]]

print(' '.join(map(str, ans)))
