answer = 0
N, S = map(int, input().split())
text = input()
arr = list(map(int, input().split()))
dict = {}
dict['A'], dict['C'], dict['G'], dict['T'] = arr

for t in text[:S]:
    dict[t] -= 1

if all(i <= 0 for i in dict.values()):
    answer += 1

for i in range(1, N-S+1):

    a = text[i-1]
    b = text[i+S-1]

    dict[a] += 1
    dict[b] -= 1

    if all(i <= 0 for i in dict.values()):
        answer += 1

print(answer)
