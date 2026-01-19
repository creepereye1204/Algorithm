from collections import deque


def solve(graph, a, b):
    visited = set()
    removed = {(a, b), (b, a)}
    q = deque([1])
    while q:
        node = q.popleft()

        visited.add(node)
        next_nodes = graph[node]
        for next_node in next_nodes:

            if (node, next_nodes) not in removed and (next_nodes, node) not in removed and next_node not in visited:
                visited.add(next_node)
                removed.add((next_node, node))
                removed.add((node, next_node))
                q.append(next_node)

    return len(visited)


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)

    for wire in wires:
        a, b = wire
        answer = min(answer, abs(n-solve(graph, a, b)))

    return answer
