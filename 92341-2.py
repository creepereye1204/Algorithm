def convert(time):
    hh, mm = map(int, time.split(':'))
    return hh*60+mm


def make(records, cars):
    for record in records:
        time, car, _ = record.split()
        time = convert(time)
        cars[car].append(time)


def result(cars, answer, fees):
    import math
    basic, start, duration, cost = fees
    for car in cars:
        if len(cars[car]) % 2 == 1:
            cars[car].append(23*60+59)
        for i in range(0, len(cars[car]), 2):
            answer[car] += cars[car][i+1]-cars[car][i]
        pay = start
        answer[car] -= basic
        if answer[car] > 0:
            answer[car] = pay+cost*math.ceil(answer[car]/duration)
        else:
            answer[car] = pay

    return [answer[key] for key in sorted(answer.keys())]


def solution(fees, records):
    from collections import defaultdict
    answer = defaultdict(int)
    cars = defaultdict(list)

    make(records, cars)
    return result(cars, answer, fees)
