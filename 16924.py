n, m = map(int, input().split())
table = [list(input()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

result = []


def fill(visited, arr):
    for a in arr:
        visited[a[0]][a[1]] = True


def find(x, y, table, n, m):

    arr = [[y, x]]
    for i in range(1, 1000):

        if -1 < x-i and x+i < m and -1 < y-i and y+i < n and table[y][x-i] == '*' and table[y][x+i] == '*' and table[y-i][x] == '*' and table[y+i][x] == '*':

            arr += [[y, x-i], [y, x+i], [y-i, x], [y+i, x]]
        else:
            break
    return arr


def check(table, visited, n, m):
    for i in range(n):
        for j in range(m):
            if (table[i][j] == '*' and visited[i][j]) or (table[i][j] == '.' and not visited[i][j]):
                continue
            return False
    return True


for i in range(n):
    for j in range(m):
        if table[i][j] == '*':
            arr = find(j, i, table, n, m)

            if len(arr) > 1:
                result.append([i+1, j+1, (len(arr)-1)//4])
                fill(visited, arr)
if check(table, visited, n, m):
    for r in result:
        print(*r)
else:
    print(-1)
