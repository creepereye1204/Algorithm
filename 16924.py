n, m = map(int, input().split())
table = [list(input()) for _ in range(n)]

result = []
visited = [[False] * m for _ in range(n)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for y in range(n):
    for x in range(m):
        if table[y][x] != '*':
            continue

        size = 0
        while True:
            size += 1
            ok = True
            for d in range(4):
                nx = x + dx[d] * size
                ny = y + dy[d] * size
                if not (0 <= nx < m and 0 <= ny < n and table[ny][nx] == '*'):
                    ok = False
                    break
            if not ok:
                size -= 1
                break

        if size >= 1:
            result.append((y + 1, x + 1, size))
            visited[y][x] = True
            for i in range(1, size + 1):
                visited[y - i][x] = True
                visited[y + i][x] = True
                visited[y][x - i] = True
                visited[y][x + i] = True

# 모든 '*'이 방문되었는지 확인
for y in range(n):
    for x in range(m):
        if table[y][x] == '*' and not visited[y][x]:
            print(-1)
            exit()

print(len(result))
for r in result:
    print(*r)
