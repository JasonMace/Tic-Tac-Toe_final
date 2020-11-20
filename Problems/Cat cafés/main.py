cafe = list()
catmax = 0
idx = 0

line = input().split()

while len(line) == 2:
    cafe.append([line[0], int(line[1])])
    line = input().split()

for i in range(0, len(cafe)):
    if cafe[i][1] > catmax:
        catmax = cafe[i][1]
        idx = i

for j in range(0, len(cafe)):
    if cafe[j][1] == catmax:
        print(cafe[j][0])

