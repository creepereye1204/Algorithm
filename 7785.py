

n = int(input())
answer = set()
for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        answer.add(name)
    else:
        answer.discard(name)
for t in sorted(list(answer), reverse=True):
    print(t)
