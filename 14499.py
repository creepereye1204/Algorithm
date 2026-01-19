N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def roll(command):
    top, bottom, north, south, west, east = dice
    if command == 1:
        dice[0], dice[1], dice[4], dice[5] = west, east, bottom, top
    elif command == 2:
        dice[0], dice[1], dice[4], dice[5] = east, west, top, bottom
    elif command == 3:
        dice[0], dice[1], dice[2], dice[3] = south, north, top, bottom
    elif command == 4:
        dice[0], dice[1], dice[2], dice[3] = north, south, bottom, top


for command in commands:
    nx, ny = x + dx[command], y + dy[command]
    if not (0 <= nx < N and 0 <= ny < M):
        continue
    x, y = nx, ny
    roll(command)
    if board[x][y] == 0:
        board[x][y] = dice[1]
    else:
        dice[1] = board[x][y]
        board[x][y] = 0
    print(dice[0])
