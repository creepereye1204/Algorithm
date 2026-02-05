import sys
sys.setrecursionlimit(10**9)


n = int(input())
arr = list(map(int, input().split()))
ops = list(map(int, input().split()))
mx = -sys.maxsize
mn = sys.maxsize


def calc(cost, j, index):
    global arr
    if j == 0:
        return cost+arr[index]
    elif j == 1:
        return cost-arr[index]
    elif j == 2:
        return cost*arr[index]
    else:
        if cost < 0:
            return -(abs(cost)//arr[index])
        return cost//arr[index]


def solve(cost, index):
    global ops, mx, mn, n
    index += 1

    if index == n:

        mx = max(mx, cost)
        mn = min(mn, cost)
        return

    for j in range(4):
        if ops[j] > 0:
            ops[j] -= 1

            solve(calc(cost, j, index), index)

            ops[j] += 1


solve(arr[0], 0)
print(mx)
print(mn)
