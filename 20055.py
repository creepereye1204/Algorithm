
from collections import deque

n, k = map(int, input().split())
container = deque(list(map(int, input().split())))
robots = deque([0]*n)
cnt = 0
answer = 1


def move(container, robots, n):

    for i in range(n-2, -1, -1):
        if container[i+1] > 0 and robots[i+1] == 0 and robots[i] == 1:
            robots[i+1] = 1
            robots[i] = 0
            container[i+1] -= 1

    robots[-1] = 0


while True:

    container.rotate(1)
    robots.rotate(1)

    robots[-1] = 0
    move(container, robots, n)
    if container[0] > 0:
        robots[0] = 1
        container[0] -= 1

    if container.count(0) >= k:
        break
    answer += 1
print(answer)
