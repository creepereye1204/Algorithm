

def init(word, m):
    temp = word[:m]
    curr = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for t in temp:
        curr[t] += 1

    return curr


def check(correct, curr):
    return all([correct[index] <= curr[index] for index in correct.keys()])


def simulate(word, m, curr, correct):
    answer = 0

    for i in range(len(word)):

        if check(correct, curr):
            answer += 1
        try:
            curr[word[i]] -= 1
            curr[word[i+m]] += 1
        except:
            print(answer)
            exit(0)


N, M = map(int, input().split())
word = input()
text = list(map(int, input().split()))
correct = {}
correct['A'] = text[0]
correct['C'] = text[1]
correct['G'] = text[2]
correct['T'] = text[3]
curr = init(word, M)
simulate(word, M, curr, correct)
