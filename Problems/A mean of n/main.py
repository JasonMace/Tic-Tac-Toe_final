length = int(input())
mylist = list()

for i in range(length):
    mylist.append(int(input()))

print(sum(mylist) / len(mylist))
