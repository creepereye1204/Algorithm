
import sys
sys.setrecursionlimit(10**9)
answer = []


def dfs(x, y, A, B, C, L, index, stack):
    if L == len(stack):
        if x > 0 and y > 1:
            global answer
            answer.append(''.join(stack))
        return

    for i in range(index, len(C)):
        stack.append(C[i])
        if C[i] in A:
            dfs(x+1, y, A, B, C, L, i+1, stack)
        else:
            dfs(x, y+1, A, B, C, L, i+1, stack)
        stack.pop()


def init(words):

    A = {'a', 'e', 'i', 'o', 'u'} & set(words)
    B = set(words) - A
    C = sorted(list(A | B))
    return A, B, C


def sol():
    global answer
    L, _ = map(int, input().split())
    words = input().split()
    A, B, C = init(words)
    dfs(0, 0, A, B, C, L, 0, [])
    for a in answer:
        print(a)


sol()
