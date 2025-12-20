N, M = map(int, input().split())
prior_nums = [0] * N
pri_dic = {i: [] for i in range(1, N+1)}
ans = {i: 0 for i in range(N)}
for _ in range(M):
    a, b = map(int, input().split())
    prior_nums[b-1] += 1
    pri_dic[a].append(b)

passed = set()
semester = 1
while len(passed) != N:
    can_course = [i for i in range(N) if prior_nums[i] == 0 and (
        i) not in passed]
    for c in can_course:
        ans[c] = semester
        passed.add(c)

        for next in pri_dic[c+1]:
            prior_nums[next-1] -= 1

    semester += 1
print(' '.join(map(str, list(ans.values()))))
