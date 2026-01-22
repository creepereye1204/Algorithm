from collections import deque

n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]


dice = [1, 3, 4, 5, 2, 6]

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]


def roll(dice, dir):
    top, east, west, south, north, bottom = dice
    if dir == 1:
        dice[1], dice[0], dice[2], dice[5] = top, west, bottom, east
    elif dir == 2:
        dice[0], dice[2], dice[5], dice[1] = east, top, west, bottom
    elif dir == 3:
        dice[0], dice[3], dice[5], dice[4] = north, top, south, bottom
    else:
        dice[4], dice[0], dice[3], dice[5] = top, south, bottom, north


cnt = 0
answer = 0
state = (0, 0, 1)
while cnt < k:
    y, x, dir = state
    if dx[dir]+x < 0 or m <= dx[dir]+x or dy[dir]+y < 0 or n <= dy[dir]+y:
        if dir == 1:
            dir = 2
        elif dir == 2:
            dir = 1
        elif dir == 3:
            dir = 4
        else:
            dir = 3
    y, x = y+dy[dir], dx[dir]+x

    roll(dice, dir)
    if table[y][x] < dice[5]:
        if dir == 1:
            dir = 3
        elif dir == 2:
            dir = 4
        elif dir == 3:
            dir = 2
        else:
            dir = 1
    elif table[y][x] > dice[5]:
        if dir == 3:
            dir = 1
        elif dir == 4:
            dir = 2
        elif dir == 2:
            dir = 3
        else:
            dir = 4
    state = (y, x, dir)
    cnt += 1
    visited = set()
    visited.add((y, x))
    temp = table[y][x]
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        for i in range(1, 5):
            x_ = dx[i]+x
            y_ = dy[i]+y
            if -1 < x_ < m and -1 < y_ < n and (y_, x_) not in visited and temp == table[y_][x_]:
                q.append((y_, x_))
                visited.add((y_, x_))

    answer += len(visited)*temp
print(answer)
