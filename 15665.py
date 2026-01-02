from itertools import product

N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))

for seq in product(arr, repeat=M):
    print(' '.join(map(str, seq)))
