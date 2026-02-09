from collections import defaultdict
T = int(input())


for _ in range(T):
    answer = 1
    wears = defaultdict(int)
    n = int(input())
    for _ in range(n):
        _, key = input().split()
        wears[key] += 1

    for value in wears.values():
        answer *= (value+1)
    print(answer-1)
