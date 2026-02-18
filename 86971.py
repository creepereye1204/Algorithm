from collections import deque


def do_bfs(graph):
    q = deque([1])
    visited = set({1})
    cnt = 0
    while q:
        cnt += 1
        node = q.popleft()

        for next in graph[node]:
            if next not in visited:
                q.append(next)
                visited.add(next)
    return cnt


def make_graph(n, wires):
    graph = [[] for _ in range(n+1)]
    for wire in wires:
        n1, n2 = wire
        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph


def solution(n, wires):
    answer = 10**9
    for i in range(n-1):
        graph = make_graph(n, wires[:i]+wires[i+1:])
        cnt = do_bfs(graph)

        answer = min(answer, abs(n-2*cnt))
    return answer
