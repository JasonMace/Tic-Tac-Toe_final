coord_x = float(input())
coord_y = float(input())

if coord_x >= 0.0:
    if coord_y >= 0.0:
        print("I")
    else:
        print("IV")
else:
    if coord_y >= 0:
        print("II")
    else:
        print("III")
