tmp = 0
mylist = list()
for num in input():
    mylist.append(int(num) + tmp)
    tmp += int(num)
print(mylist)
