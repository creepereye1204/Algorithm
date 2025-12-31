from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    visited = [-1 for _ in range(n+1)]
    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)
    q = deque([destination])
    visited[destination] = 0
    while q:
        curr_node = q.popleft()

        for next_node in graph[curr_node]:
            if visited[next_node] == -1:
                visited[next_node] = 1+visited[curr_node]
                q.append(next_node)

    return [visited[source] for source in sources]
