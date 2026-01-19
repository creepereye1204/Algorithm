from itertools import permutations
import sys

N = int(input())
base = tuple(tuple(map(int, sys.stdin.readline().split(' ')))
             for _ in range(N))

candidate = set(permutations([i for i in range(1, 10)], 3))

for b in base:
    for c in candidate:

        strike_cnt = 0
        ball_cnt = 0
        for i in range(3):
            if c[i] == int(str(b[0])[i]):
                strike_cnt += 1
            elif int(str(b[0])[i]) in c:
                ball_cnt += 1

        if strike_cnt == b[1] and ball_cnt == b[2]:
            pass
        else:
            candidate = candidate - {c}
print(len(candidate))
