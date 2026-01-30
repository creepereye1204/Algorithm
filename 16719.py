def solve(s, l, r, visited):
    if l > r:
        return

    idx = min(range(l, r+1), key=lambda i: s[i])
    visited[idx] = True
    print("".join([s[i] for i in range(len(s)) if visited[i]]))

    solve(s, idx+1, r, visited)

    solve(s, l, idx-1, visited)


s = input().strip()
visited = [False] * len(s)
solve(s, 0, len(s)-1, visited)
