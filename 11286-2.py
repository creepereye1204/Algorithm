import heapq
import sys

input = sys.stdin.readline
n = int(input())
answer = []
for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(answer, (abs(num), num))
    elif answer:
        _, num = heapq.heappop(answer)
        print(num)
    else:
        print(num)
