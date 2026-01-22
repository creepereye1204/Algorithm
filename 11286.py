import sys
import heapq
input = sys.stdin.readline

k = int(input())
q = []

for _ in range(k):
    num = int(input())
    if num == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(num), num))
