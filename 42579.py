from collections import defaultdict


def solution(genres, plays):
    answer = []
    orders = defaultdict(int)
    times = defaultdict(list)
    for i in range(len(plays)):
        orders[genres[i]] += plays[i]
        times[genres[i]].append([plays[i], i])
    orders = sorted(orders.items(), key=lambda x: -x[1])
    for order in orders:
        r = sorted(times[order[0]], key=lambda x: (-x[0], x[1]))
        answer.append(r[0][1])
        if len(r) > 1:
            answer.append(r[1][1])

    return answer
