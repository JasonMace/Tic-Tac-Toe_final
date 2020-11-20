dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]

word = input()
state = False
for tmp in dictionary:
    if tmp == word:
        state = True
print("Correct" if state else "Incorrect")
