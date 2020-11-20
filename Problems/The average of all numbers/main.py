# put your python code here
begin = int(input())
end = int(input())
res = 0
count = 0

for i in range(begin, end + 1):
    if i % 3 == 0:
        res += i
        count += 1

print(res / count)
