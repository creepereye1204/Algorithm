from collections import Counter


def solution(weights):
    answer = 0
    weights = Counter(weights)
    for key, value in weights.items():

        answer += value*(value-1)/2

        if key*1.5 in weights:
            answer += weights[key*1.5]*value

        if key*(4/3) in weights:
            answer += weights[key*(4/3)]*value

        if key*2 in weights:
            answer += weights[key*2]*value
    return answer
