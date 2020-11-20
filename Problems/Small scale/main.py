inp = ""
numbers = list()

while inp != ".":
    inp = input()
    if inp == ".":
        break
    num = float(inp)
    numbers.append(num)
print(min(numbers))
