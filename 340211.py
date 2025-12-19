from collections import Counter


def move_one_step(current, target):
    x, y = current
    tx, ty = target

    if x < tx:
        x += 1
    elif x > tx:
        x -= 1
    elif y < ty:
        y += 1
    else:
        y -= 1

    return [x, y]


def solution(points, routes):
    answer = 0
    arr = [[points[route[i]-1].copy() for i in range(len(route))][::-1]
           for route in routes]

    l = len(routes)
    visited = [True]*l
    while any(visited):
        group = []
        for i, route in enumerate(arr):
            if not visited[i]:
                continue

            current = route[-1]
            target = route[-2] if len(route) > 1 else None

            if target and current == target:
                route.pop()
                if len(route) == 1:
                    visited[i] = False
                current = route[-1]

            group.append(tuple(current))

        values = Counter(group).values()
        answer += sum([1 if value > 1 else 0 for value in values])

        for i, route in enumerate(arr):
            if visited[i]:
                route[-1] = move_one_step(route[-1], route[-2])

    return answer
