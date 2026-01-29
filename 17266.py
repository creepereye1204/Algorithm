import math

N = int(input())
M = int(input())
arr = list(map(int, input().split()))


max_gap = 0
for i in range(M-1):
    gap = arr[i+1] - arr[i]
    max_gap = max(max_gap, math.ceil(gap / 2))


left_gap = arr[0] - 0
right_gap = N - arr[-1]

answer = max(max_gap, left_gap, right_gap)
print(answer)
