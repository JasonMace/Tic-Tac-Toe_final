score = int(input())
maximum = int(input())

grades = ["A", "B", "C", "D", "F"]
mins = [90, 80, 70, 60, 0]

for i in range(len(mins)):
    if (score / maximum) * 100 >= mins[i]:
        print(grades[i])
        exit()
