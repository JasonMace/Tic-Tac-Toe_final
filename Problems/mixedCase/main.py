text = input().split()
tmp = []

for i in range(0, len(text)):
    if i == 0:
        tmp.append(text[i])
    else:
        tmp.append(text[i].capitalize())

print("".join(tmp))
