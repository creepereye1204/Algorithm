answer = [True]*10001
for i in range(1, 10001):
    t = i+sum(list(map(int, list(str(i)))))

    if t < 10001:
        answer[t] = False

for i in range(1, 10001):
    if answer[i]:
        print(i)
