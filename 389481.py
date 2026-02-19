from string import ascii_lowercase

A = {a: idx+1 for idx, a in enumerate(ascii_lowercase)}


def convert(text):

    num = 0
    for ch in text:
        num = num * 26 + A[ch]
    return num


def deconvert(num):

    temp = []
    while num > 0:
        num, rem = divmod(num-1, 26)
        temp.append(ascii_lowercase[rem])
    return ''.join(reversed(temp))


def solution(n, bans):
    ban_nums = sorted(convert(b) for b in bans)
    shift = 0
    for b in ban_nums:
        if b <= n + shift:
            shift += 1
        else:
            break
    return deconvert(n + shift)
