# put your python code here
count = 0


def best_counter(array):
    global count
    for tmp in array:
        if tmp == "A":
            count += 1


results = input()
grades = results.split()
best_counter(grades)
print(round(count / len(grades), 2))
