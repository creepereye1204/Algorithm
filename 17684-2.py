def init():
    import string
    return {char: index+1 for index, char in enumerate(string.ascii_uppercase)}


def find(stack, answer, table):
    temp = []
    while stack:
        char = stack.pop()
        temp.append(char)
        if ''.join(temp) not in table:

            table[''.join(temp)] = len(table)+1
            stack.append(temp.pop())
            break
    answer.append(table[''.join(temp)])
    return stack


def solution(msg):
    answer = []
    table = init()
    stack = list(msg)[::-1]
    while find(stack, answer, table):
        pass
    return answer
