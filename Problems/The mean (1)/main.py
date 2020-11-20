numbers = list()
elem = 0

while elem != ".":
    elem = input()
    if elem != ".":
        numbers.append(int(elem))
    else:
        break

print(sum(numbers) / len(numbers))
