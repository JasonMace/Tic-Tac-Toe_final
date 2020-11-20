word = input()
res = ""
flag = True
for char in word:
    if flag:
        res += char.lower()
        flag = False
    elif char.islower():
        res += char
    else:
        res = res + "_" + char.lower()
print(res)
