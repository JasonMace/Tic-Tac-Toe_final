prime_flag = False

num = int(input())
if num == 1:
    print("This number is not prime")
    exit()
if num != 1:
    for i in range(2, num):
        if prime_flag:
            break
        if num % i == 0:
            prime_flag = True
            print("This number is not prime")
            break

if not prime_flag:
    print("This number is prime")
