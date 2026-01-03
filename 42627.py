import heapq


def solution(jobs):
    answer = time = 0
    q = [(*job, i) for i, job in enumerate(jobs)]
    heapq.heapify(q)
    tasks = []

    while q or tasks:
        while q:
            temp = heapq.heappop(q)
            if time < temp[0]:
                heapq.heappush(q, temp)
                break
            task = (temp[1], temp[0], temp[2])
            heapq.heappush(tasks, task)

        if not tasks and q:
            temp = heapq.heappop(q)
            heapq.heappush(q, temp)
            time = temp[0]
            continue

        duration, start, index = heapq.heappop(tasks)
        answer += time - start + duration
        time += duration

    return answer // len(jobs)
