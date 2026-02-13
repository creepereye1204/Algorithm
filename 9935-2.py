text = input()
bomb = list(input())
answer = []
for t in text:
    answer.append(t)
    if len(text) >= len(bomb) and answer[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            answer.pop()
print(''.join(answer) if answer else 'FRULA')
