import sys
from collections import deque
input = sys.stdin.readline

current = 0
back = deque([])
front = []
n, q, c = map(int, input().split())
sizes = [0]+list(map(int, input().split()))

for _ in range(q):
    work = input().split()
    if work[0] == 'B':
        if not back:
            continue
        front.append(current)
        current = back.pop()
        continue
    if work[0] == 'F':
        if not front:
            continue
        back.append(current)
        current = front.pop()
        continue
    if work[0] == 'C':
        if not back:
            continue
        temp = deque([back[0]])
        for i in range(1, len(back)):
            if back[i] == back[i-1]:
                c += sizes[back[i]]
                continue
            else:
                temp.append(back[i])
        back = temp
        continue
    # Access
    # 앞 삭제
    for size in front:
        c += sizes[size]
    front = []
    if current != 0:
        back.append(current)
    current = int(work[1])
    c -= sizes[current]
    while c < 0:  # 초과시
        num = back.popleft()
        c += sizes[num]
print(current)
if not back:
    print(-1)
else:
    for i in range(len(back)-1, -1, -1):
        print(back[i], end=' ')
    print()
if not front:
    print(-1)
else:
    for i in range(len(front)-1, -1, -1):
        print(front[i], end=' ')
