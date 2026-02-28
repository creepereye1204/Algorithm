

def init():
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    commmands = [list(map(int, input().split())) for _ in range(M)]
    cloud = [[False]*N for _ in range(N)]
    cloud[N-1][0] = True
    cloud[N-1][1] = True
    cloud[N-2][0] = True
    cloud[N-2][1] = True
    return table, commmands, cloud


def move(commmand, cloud):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    N = len(cloud)
    temp = [[False]*N for _ in range(N)]
    dir, iter = commmand
    dir -= 1

    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                x = (iter*dx[dir]+j) % N
                y = (iter*dy[dir]+i) % N
                temp[y][x] = True
    return temp


def rain(cloud, table):
    N = len(cloud)
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                table[i][j] += 1


def magic(cloud, table):
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]
    N = len(cloud)
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                for v in range(4):
                    x = dx[v]+j
                    y = dy[v]+i
                    if -1 < x < N and -1 < y < N and table[y][x] > 0:
                        table[i][j] += 1


def make(cloud, table):
    N = len(cloud)
    temp = [[False]*N for _ in range(N)]
    for i in range(len(cloud)):
        for j in range(len(cloud)):
            if not cloud[i][j] and table[i][j] >= 2:
                temp[i][j] = True
                table[i][j] -= 2

    return temp


def simulate(table, commmands, cloud):
    for commmand in commmands:
        cloud = move(commmand, cloud)
        rain(cloud, table)
        magic(cloud, table)
        cloud = make(cloud, table)


def result(table):
    return sum(sum(t) for t in table)


def answer():
    table, commmands, cloud = init()
    simulate(table, commmands, cloud)
    return result(table)


print(answer())
