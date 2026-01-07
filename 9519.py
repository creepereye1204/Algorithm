n = int(input())
s = input()

loop = [s]
visi = set([s])

for _ in range(n):
    s = s[::2] + s[1::2][::-1]
    if s in visi:
        break
    loop.append(s)
    visi.add(s)

print(loop[n % len(loop)])
