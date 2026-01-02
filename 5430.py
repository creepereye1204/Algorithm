from collections import deque
for _ in range(int(input())):

    ops = input()
    input()
    arr = input()[1:-1]
    if arr:
        arr = deque(map(int, arr.split(',')))

    toggle = False
    for op in ops:

        if op == 'R':
            toggle = not toggle

        elif not arr:
            print('error')
            break
        elif not toggle:

            arr.popleft()

        else:
            arr.pop()

    else:
        if not arr:
            print('[]')
            continue

        if ops.count('R') % 2 == 1:
            arr = reversed(arr)
        arr = ','.join(map(str, arr))
        print('['+arr+']')
