def closest_higher_mod_5(x):
    y = x
    while y % 5 != 0:
        y += 1
    return y
