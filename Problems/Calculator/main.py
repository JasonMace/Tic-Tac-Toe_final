# put your python code here
first_number = float(input())
second_number = float(input())
operation = input()
if second_number == 0.0 and operation in ["mod", "div", "/"]:
    print("Division by 0!")
else:
    if operation == "+":
        print(first_number + second_number)
    elif operation == "-":
        print(first_number - second_number)
    elif operation == "/":
        print(first_number / second_number)
    elif operation == "*":
        print(first_number * second_number)
    elif operation == "mod":
        print(first_number % second_number)
    elif operation == "pow":
        print(first_number ** second_number)
    elif operation == "div":
        print(first_number // second_number)
