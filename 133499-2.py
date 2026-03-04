def check(words, b):
    for word in words:

        if 2*word in b:
            return False
    return True


def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        if not check(words, b):
            continue

        for word in words:
            b = b.replace(word, ' ')

        if b.strip():

            continue
        answer += 1
    return answer
