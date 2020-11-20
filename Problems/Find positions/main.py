# put your python code here
numbers = input().split()
num = input()
indexes = []

for i, j in enumerate(numbers):
    if j == num:
        indexes.append(str(i))

print(" ".join(indexes) if len(indexes) > 0 else "not found")
