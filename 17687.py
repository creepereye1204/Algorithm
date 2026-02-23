def convert(num, n):

    if not num:
        return ''
    nums = '0123456789ABCDEF'
    num, mod = divmod(num, n)
    return convert(num, n)+nums[mod]


def solution(n, t, m, p):
    answer = ''.join(
        [convert(i, n) if i != 0 else '0' for i in range(t*m)])[p-1::m][:t]

    return answer
