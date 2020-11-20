scores = input().split()
# put your python code here
stepcounter = 0
i_counter = 0

for answer in scores:
    if answer == "I":
        i_counter += 1
    if i_counter == 3:
        stepcounter += 1
        print("Game over\n" + str(stepcounter - i_counter))
        break
    stepcounter += 1

if i_counter < 3:
    print("You won\n" + str(stepcounter - i_counter))
