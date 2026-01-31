

answer = 0
N, S = map(int, input().split())
arr = [0]+list(map(int, input().split()))
for i in range(1, N+1):
    arr[i] += arr[i-1]


for i in range(1, N+1):
    for j in range(i, N+1):

        if arr[j]-arr[j-i] == S:
            answer += 1
print(answer)
