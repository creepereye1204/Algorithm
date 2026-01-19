from collections import deque


def rotate(chains, idx, direction):
    chains[idx].rotate(direction)


def solve(chains, idx, direction):
    n = len(chains)
    dirs = [0] * n
    dirs[idx] = direction

    for i in range(idx-1, -1, -1):
        if chains[i][2] != chains[i+1][6]:
            dirs[i] = -dirs[i+1]
        else:
            break

    for i in range(idx+1, n):
        if chains[i-1][2] != chains[i][6]:
            dirs[i] = -dirs[i-1]
        else:
            break

    for i in range(n):
        if dirs[i] != 0:
            rotate(chains, i, dirs[i])


def get_result(chains):
    scores = [1, 2, 4, 8]
    return sum(chains[i][0] * scores[i] for i in range(4))


def main():
    chains = [deque(map(int, input().strip())) for _ in range(4)]
    k = int(input())
    plays = [tuple(map(int, input().split())) for _ in range(k)]

    for idx, direction in plays:
        solve(chains, idx-1, direction)

    print(get_result(chains))


if __name__ == "__main__":
    main()
