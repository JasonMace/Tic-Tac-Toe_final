words = input().split('_')
for i, word in enumerate(words):
    words[i] = word.capitalize()

print("".join(words))
