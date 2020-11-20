lines = int(input())
mylist = list()

for i in range(lines):
    elem = input()
    final = elem.split()
    if final[1] == "win":
        mylist.append(final[0])

print(mylist)
print(len(mylist))
