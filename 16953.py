

s, e = map(int, input().split())
answer = 1
while s < e:
    if e % 10 == 1:
        e //= 10
    elif e % 2 == 1:
        print(-1)
        exit(0)
    else:
        e //= 2
    answer += 1
if e == s:
    print(answer)
else:
    print(-1)
