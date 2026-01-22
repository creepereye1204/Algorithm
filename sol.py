# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]


# cleaned = [[False]*M for _ in range(N)]
# cnt = 0


# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# while True:

#     if not cleaned[r][c]:
#         cleaned[r][c] = True
#         cnt += 1

#     found = False
#     for i in range(4):
#         nd = (d + 3 - i) % 4
#         nr, nc = r + dx[nd], c + dy[nd]
#         if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0 and not cleaned[nr][nc]:
#             r, c, d = nr, nc, nd
#             found = True
#             break

#     if found:
#         continue

#     back_dir = (d + 2) % 4
#     br, bc = r + dx[back_dir], c + dy[back_dir]
#     if 0 <= br < N and 0 <= bc < M and graph[br][bc] == 0:
#         r, c = br, bc
#     else:
#         print(cnt)
#         break
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

answer = float('inf')
curr_sum = 0
left = 0

for right in range(n):
    curr_sum += arr[right]

    while curr_sum >= s:
        answer = min(answer, right - left + 1)
        curr_sum -= arr[left]
        left += 1

print(0 if answer == float('inf') else answer)
