import sys


input = sys.stdin.readline
answer = ''


def find_text(text, word):
    global answer
    t = len(text)
    w = len(word)
    for i in range(t-w+1):
        if text[i:i+w] == word:
            return True


def decode_text(text, n):
    return ''.join([chr(((ord(t)+n-97) % 26)+97) for t in text])


original = input()
n = int(input())
words = [input() for _ in range(n)]
for i in range(100):
    text = decode_text(original, i)
    for word in words:
        if find_text(text, word):
            print(text)
            exit(0)
