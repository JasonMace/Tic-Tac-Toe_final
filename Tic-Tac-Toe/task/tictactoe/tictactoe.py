matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
symbols = ["X", "O"]
coord = []
step = True
finish = False
draw = False
breaker = False


def printFields():
    print("---------")
    print("|", " ".join(matrix[0]), "|")
    print("|", " ".join(matrix[1]), "|")
    print("|", " ".join(matrix[2]), "|")
    print("---------")


def printStep():
    global step
    global matrix
    coordRaw = input("Enter the coordinates: > ").split()
    coordpre = [int(coordRaw[0]), int(coordRaw[1])]

    if len(coordRaw) == 1 or len(coordRaw[0]) > 1 or len(coordRaw[1]) > 1:
        print("You should enter numbers!")
        printStep()

    if coordpre[0] < 1 or coordpre[0] > 3 or coordpre[1] < 1 or coordpre[1] > 3:
        print("Coordinates should be from 1 to 3!")
    else:
        coordy = coordConverter(coordpre)
        if matrix[coordy[0]][coordy[1]] == " ":
            if step:
                matrix[coordy[0]][coordy[1]] = "X"
                step = False
            elif not step:
                matrix[coordy[0]][coordy[1]] = "O"
                step = True
            endcheck()
            if not finish:
                printFields()
        elif matrix[coordy[0]][coordy[1]] in symbols:
            print("This cell is occupied! Choose another one!")


def coordConverter(coord):
    second = coord[0] - 1
    if coord[1] == 1:
        first = 2
    elif coord[1] == 2:
        first = 1
    elif coord[1] == 3:
        first = 0
    return [first, second]



def endcheck():
    linebool = False
    global finish
    global draw
    counter = 0
    for i in range(0, 3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] and (matrix[i][0] in symbols and matrix[i][1] in symbols and matrix[i][2] in symbols):
            finish = True
    for j in range(0, 3):
        if matrix[0][j] == matrix[1][j] == matrix[2][j] and (matrix[0][j] in symbols and matrix[1][j] in symbols and matrix[2][j] in symbols):
            finish = True
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and (matrix[0][0] in symbols and matrix[1][1] in symbols and matrix[2][2] in symbols):
        finish = True
    if matrix[2][0] == matrix[1][1] == matrix[0][2] and (matrix[2][0] in symbols and matrix[1][1] in symbols and matrix[0][2] in symbols):
        finish = True
    for k in matrix:
        for j in k:
            if j in symbols:
                counter += 1
    if counter == 9:
        draw = True




printFields()
while not finish and not draw:
    printStep()
printFields()
if draw and not finish:
    print("Draw")
else:
    print("O wins" if step else "X wins")



