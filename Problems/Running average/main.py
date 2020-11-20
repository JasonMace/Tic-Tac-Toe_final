mylist = [int(char) for char in input()]
reslist = []
idx = 0
while idx + 2 <= len(mylist):
    reslist.append((mylist[idx] + mylist[idx + 1]) / 2)
    idx += 1
print(reslist)
