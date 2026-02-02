def solution(enroll, referral, seller, amount):
    n = len(enroll)
    workers = {name: i for i, name in enumerate(enroll)}
    parent = [-1] * n
    for i, r in enumerate(referral):
        if r != '-':
            parent[i] = workers[r]

    answer = [0] * n

    for s, a in zip(seller, amount):
        money = a * 100
        idx = workers[s]
        while idx != -1 and money > 0:
            give = money // 10
            keep = money - give
            answer[idx] += keep
            idx = parent[idx]
            money = give

    return answer
