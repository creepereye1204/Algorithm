
def solution(friends, gifts):
    table = {friend: {friend: 0 for friend in friends} for friend in friends}
    jisu = {friend: 0 for friend in friends}
    answer = {friend: 0 for friend in friends}

    for gift in gifts:
        giver, taker = gift.split()
        table[giver][taker] += 1

    for giver in friends:
        jisu[giver] = sum(table[giver].values())
        for taker in friends:
            jisu[giver] -= table[taker][giver]

        for taker in friends:
            if table[giver][taker] > table[taker][giver]:
                answer[giver] += 1
            elif table[giver][taker] == table[taker][giver] and jisu[giver] > jisu[taker]:
                answer[giver] += 1

    return max(answer.values())
