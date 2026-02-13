

from collections import deque
n = int(input())
arr = list(map(int, input().split()))
q = deque([(num, idx+1) for idx, num in enumerate(arr)])


while q:
    num, idx = q.popleft()
    print(idx, end=' ')
    if num > 0:

        num -= 1
    q.rotate(-num)
