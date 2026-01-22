import sys
answer = sys.maxsize
n, s = map(int, input().split())
arr = list(map(int, input().split()))
index = 0
sum = 0
for i in range(n):

    sum += arr[i]
    if sum < s:
        continue

    while index < n and sum-arr[index] >= s:

        sum -= arr[index]
        index += 1

    answer = min(answer, i-index+1)

print(0 if answer == sys.maxsize else answer)
