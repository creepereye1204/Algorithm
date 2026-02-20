def s1(text):
    if not text:
        return text
    return s2(text)


def s2(text):
    a, b = 0, 0
    for i in range(len(text)):
        if text[i] == '(':
            a += 1
        else:
            b += 1
        if a == b:
            break
    u, v = text[:i+1], text[i+1:]
    return s3(u, v)


def s3(u, v):
    stack = []
    for c in u:

        if c == '(':
            stack.append(c)
        else:
            if not stack or stack[-1] != '(':
                return s4(u, v)
            else:
                stack.pop()

    return u+s1(v)


def s4(u, v):

    return '('+s1(v)+')'+''.join([')' if c == '(' else '(' for c in u[1:-1]])


def solution(p):

    return s1(p)
