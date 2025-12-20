from collections import Counter
from functools import reduce

from operator import mul
N = int(input())
for _ in range(N):
    M = int(input())

    arr = Counter([input().split()[1]
                   for _ in range(M)])

    if len(arr) > 1:
        print(reduce(lambda x, y: (x+1)*(y+1), arr.values())-1)
    else:
        print(M)
