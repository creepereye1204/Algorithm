import copy
from collections import deque
N, M, T = map(int, input().split())
table = [input() for _ in range(N)]
q = deque([[(0, N-1)]])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0
while q:
    node = q.popleft()
    x, y = node[-1]
    for i in range(4):
        x_ = dx[i]+x
        y_ = dy[i]+y
        if (x_, y_) not in node and -1 < x_ < M and -1 < y_ < N and table[y_][x_] != 'T':

            temp = copy.deepcopy(node)
            temp.append((x_, y_))
            if x_ == M-1 and y_ == 0:
                if len(temp) == T:
                    answer += 1

                continue
            q.appendleft(temp)
if N == 1 and M == 1 and table[0][0] == 'T':
    print(1)
else:
    print(answer)
