synthesis = float(input())

if 2 <= synthesis <= 3:
    print("Synthetic")
else:
    print("Analytic" if synthesis < 2 else "Polysynthetic")
