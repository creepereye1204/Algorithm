from string import ascii_lowercase


def convert(num):
    stack = []
    while num > 0:
        num, rem = divmod(num-1, 26)
        stack.append(ascii_lowercase[rem])
    return ''.join(stack[::-1])


def deconvert(text):
    ch = {c: idx+1 for idx, c in enumerate(ascii_lowercase)}
    num = 0
    for t in text:
        num = num*26+ch[t]
    return num


def solution(n, bans):

    bans = sorted(list(map(deconvert, bans)))

    for ban in bans:
        if ban <= n:
            n += 1
        else:
            break

    return convert(n)
