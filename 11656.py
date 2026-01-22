text = input()
for t in sorted([text[i:] for i in range(len(text))]):
    print(t)
