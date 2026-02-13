text = input()
l = len(text)
toggle = True
if l % 2 == 0:
    toggle = True
else:
    toggle = False

for i in range(round(l/2), l):
    if toggle and text[-(l-i):][::-1] == text[i-(l-i):i]:
        print()
        exit()

    if not toggle and text[:l//2][::-1] == text[l//2+1:]:
        exit()
    toggle = not toggle
