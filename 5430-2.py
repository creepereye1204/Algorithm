from collections import deque
T = int(input())
for _ in range(T):
    commands = input()
    _ = input()
    text = input()[1:-1]
    if text:
        text = deque(list(map(int, text.split(','))))
    else:
        text = ''

    left = True
    for command in commands:
        if command == 'R':

            left = not left
        elif text:
            if left:
                text.popleft()
            else:
                text.pop()
        else:
            print('error')
            break
    else:
        text = list(text)
        if not left and text:
            text = text[::-1]

        print('['+','.join(map(str, text))+']')
