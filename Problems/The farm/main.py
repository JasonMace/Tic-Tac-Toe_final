animals = ["chicken", "goat", "pig", "cow", "sheep"]
prices = [23, 678, 1296, 3848, 6769]

cash = int(input())

for i in range(len(prices)):
    if cash < prices[0]:
        print("None")
        exit()
    if cash == prices[i]:
        result = cash // prices[i]
        word = str(result) + " " + animals[i]
        print(word + "s" if result > 1 else word)
        exit()
    if cash > prices[4]:
        result = cash // prices[4]
        word = str(result) + " " + animals[4]
        print(word)
        exit()
    elif cash < prices[i]:
        result = cash // prices[i - 1]
        word = str(result) + " " + animals[i - 1]
        print(word + "s" if result > 1 else word)
        exit()
