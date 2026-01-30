def solution(schedules, timelogs, startday):
    answer = 0

    l = len(schedules)
    for i in range(l):
        hh, mm = divmod(schedules[i], 100)

        if 59 < mm+10:
            hh += 1
            mm -= 50
        else:
            mm += 10
        schedules[i] = hh*100+mm
    days = [[0]*7 for _ in range(l)]
    for i in range(l):
        for j in range(7):
            days[i][(j+startday-1) % 7] = timelogs[i][j]

    for i in range(l):
        for j in range(5):
            if schedules[i] < days[i][j]:
                break
        else:
            answer += 1
    return answer
