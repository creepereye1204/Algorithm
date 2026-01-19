

from collections import deque

n = int(input())
k = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
time = 0
state = 0


table = [[0]*n for _ in range(n)]
table[0][0] = 1

stack = deque([(0, 0)])

for _ in range(k):
    y, x = map(int, input().split())
    table[y-1][x-1] = 2

m = int(input())
dirs = deque([])
for _ in range(m):
    minute, dir = input().split()
    dirs.append((int(minute), dir))


q = deque([(0, 0)])


def f2(dirs, state, time):

    while dirs and dirs[0][0] == time:
        _, dir = dirs.popleft()
        if dir == 'D':
            state = (state+1) % 4
        else:
            state = (state-1) % 4
    return state


while q:
    time += 1

    y, x = q.popleft()

    x += dx[state]
    y += dy[state]

    if x < 0 or n <= x or y < 0 or n <= y or table[y][x] == 1:

        break
    if table[y][x] == 0 and stack:
        y_, x_ = stack.popleft()
        table[y_][x_] = 0

    table[y][x] = 1
    stack.append((y, x))
    state = f2(dirs, state, time)
    q.append((y, x))

print(time)
