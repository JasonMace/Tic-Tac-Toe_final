chars = input().lower()

for letter in chars:
    if not letter.isalpha():
        break
    if letter in ["a", "e", "i", "o", "u"]:
        print("vowel")
    else:
        print("consonant")
