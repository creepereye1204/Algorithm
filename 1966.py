from collections import deque

t = int(input())  # 테스트케이스 수

for _ in range(t):
    n, m = map(int, input().split())  # 문서 개수, 궁금한 문서 위치
    priorities = list(map(int, input().split()))

    queue = deque([(p, i) for i, p in enumerate(priorities)])
    order = 0

    while queue:
        cur = queue.popleft()
        # 현재 문서보다 중요도가 높은 문서가 있는지 확인
        if any(cur[0] < q[0] for q in queue):
            queue.append(cur)
        else:
            order += 1
            if cur[1] == m:  # 내가 찾는 문서라면
                print(order)
                break
