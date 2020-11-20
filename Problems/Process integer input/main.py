# put your python code here

num = "0"
while True:
    num = int(input())
    if num < 10:
        continue
    elif num > 100:
        break
    else:
        print(num)
