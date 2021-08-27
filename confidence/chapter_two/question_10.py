import math


while True:

    number = int(input("Enter a number"))
    root = math.sqrt(number)

    if int(root) ** 2 == number:
        print(number, " is a Perfect Square")
        break
    else:
        print(number, " is not a Perfect Square")
