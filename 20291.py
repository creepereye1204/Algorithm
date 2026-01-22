from collections import defaultdict
n = int(input())
answer = defaultdict(int)
for _ in range(n):
    _, ext = input().split('.')
    answer[ext] += 1
for file in sorted(answer.keys()):
    print(file, answer[file])
