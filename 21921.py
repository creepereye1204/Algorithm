
_, x = map(int, input().split())
arr = list(map(int, input().split()))

count = sum(arr[:x])

y = [count]
for i in range(x, len(arr)):
    count = count-arr[i-x]+arr[i]

    y.append(count)

answer = max(y)
if answer == 0:
    print('SAD')
else:
    print(answer)
    print(y.count(answer))
