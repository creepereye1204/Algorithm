from collections import deque


def do_bfs(N, K):
    visited = [0] * 100001

    q = deque([N])
    while q:
        v = q.popleft()
        if v == K:
            return visited[K]

        for o in (v - 1, v + 1, 2 * v):
            if 0 <= o < 100001 and not visited[o]:
                visited[o] = 1 + visited[v]
                q += [o]


N, K = map(int, input().split(" "))
print(do_bfs(N, K))
