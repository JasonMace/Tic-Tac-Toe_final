coord_x = int(input())
coord_y = int(input())

if (coord_x >= 2 and coord_y >= 2) and (coord_x <= 7 and coord_y <= 7):
    print(8)
elif (coord_x == 1 or coord_x == 8) and (coord_y == 1 or coord_y == 8):
    print(3)
elif ((coord_y == 1 or coord_y == 8) and 1 < coord_x < 8) or ((coord_x == 1 or coord_x == 8) and 1 < coord_y < 8):
    print(5)
