import math

sentinel = 0
while sentinel != -1:
    number = int(input("Enter number: "))
    root = math.sqrt(number)
    if root ** 2 == number:
        print("It is a perfect square")
        sentinel = -1
    else:
        print("Wrong number.Enter number again")
