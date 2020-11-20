text = input()
palind = True
i = len(text) - 1
j = 0

while i > -1:
    if text[i] == text[j]:
        i = i - 1
        j += 1
    else:
        palind = False
        break


if not palind:
    print("Not palindrome")
else:
    print("Palindrome")
