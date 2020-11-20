inp_a = int(input())
inp_b = int(input())
inp_h = int(input())

if inp_a <= inp_h <= inp_b:
    print("Normal")
    exit()
print("Excess" if inp_h > inp_b else "Deficiency")
