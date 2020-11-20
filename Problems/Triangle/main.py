rounds = int(input())

for i in range(rounds):
    print(((i + (i + 1)) * "#").center(rounds + rounds - 1))
