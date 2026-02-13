from collections import deque

start, end = map(int, input().split())
visited = {start}
q = deque([(start, 0)])

while q:
    node, score = q.popleft()
    if node == end:
        print(score)
        break
    for num in (node-1, node+1, node*2):
        if 0 <= num <= 100000 and num not in visited:
            visited.add(num)
            q.append((num, score+1))
