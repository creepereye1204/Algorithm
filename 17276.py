

def solution(table, n):
    one = [table[i][i] for i in range(n)]
    two = [table[i][n//2] for i in range(n)]
    tree = [table[i][n-i-1] for i in range(n)]
    four = table[n//2][::-1]
    for i in range(n):
        table[i][n//2] = one[i]
        table[i][n-i-1] = two[i]
        table[n//2][n-i-1] = tree[i]
        table[n-i-1][n-i-1] = four[i]


T = int(input())
for _ in range(T):
    n, d = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]

    d = (360+d)//45

    for _ in range(d):
        solution(table, n)

    for r in table:
        print(" ".join(map(str, r)))
