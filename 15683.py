import sys
input = sys.stdin.readline

# CCTV 방향 정의
directions = {
    1: [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],
    2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
    3: [[(0, 1), (-1, 0)], [(0, 1), (1, 0)], [(0, -1), (-1, 0)], [(0, -1), (1, 0)]],
    4: [[(0, 1), (0, -1), (1, 0)], [(0, 1), (0, -1), (-1, 0)],
        [(1, 0), (-1, 0), (0, -1)], [(1, 0), (-1, 0), (0, 1)]],
    5: [[(0, 1), (0, -1), (1, 0), (-1, 0)]]
}


def watch(board, x, y, dirs, N, M):
    for dx, dy in dirs:
        nx, ny = x, y
        while True:
            nx += dx
            ny += dy
            if not (0 <= nx < M and 0 <= ny < N):
                break
            if board[ny][nx] == 6:
                break
            if board[ny][nx] == 0:
                board[ny][nx] = '#'


def dfs(index, cctv, board, N, M):
    if index == len(cctv):
        return sum(row.count(0) for row in board)
    x, y, t = cctv[index]
    res = 1e9
    for dirs in directions[t]:
        new_board = [row[:] for row in board]
        watch(new_board, x, y, dirs, N, M)
        res = min(res, dfs(index+1, cctv, new_board, N, M))
    return res


def main():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cctv = [(j, i, board[i][j]) for i in range(N)
            for j in range(M) if board[i][j] not in (0, 6)]
    print(dfs(0, cctv, board, N, M))


if __name__ == "__main__":
    main()
