def solution(picks, minerals):
    answer = 0
    s = min(len(minerals), sum(picks)*5)
    costs = {"diamond": 25, "iron": 5, "stone": 1}
    stack = sorted([minerals[i:i+5] for i in range(0, s, 5)],
                   key=lambda xx: (-max(costs[x] for x in xx), -sum(costs[x] for x in xx)))
    for ss in stack:
        if picks[0]:
            picks[0] -= 1
            answer += len(ss)
        elif picks[1]:
            picks[1] -= 1
            answer += sum(5 if s == "diamond" else 1 for s in ss)
        else:
            picks[2] -= 1
            answer += sum(costs[s] for s in ss)

    return answer
