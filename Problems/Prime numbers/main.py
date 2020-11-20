prime_numbers = list()

for i in range(2, 1001):
    helpother = list()
    for j in range(2, i - 1):
        if j != i:
            helpother.append(i % j)
    if all(helpother):
        prime_numbers.append(i)
