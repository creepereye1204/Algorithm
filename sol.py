from string import ascii_lowercase
texts = ascii_lowercase
n = 2
for i in range(len(texts)-n+1):
    print(texts[i:i+n])
