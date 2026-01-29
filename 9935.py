text = input().strip()
word = input().strip()
stack = []
length = len(word)

for ch in text:
    stack.append(ch)

    if len(stack) >= length and ''.join(stack[-length:]) == word:
        for _ in range(length):
            stack.pop()

result = ''.join(stack)
print(result if result else "FRULA")
