import math


number = int(input("Enter a number"))
root = math.sqrt(number)

if int(root + 0.5) ** 2 == number:
    print(number, " is a Perfect Square")
else:
    print(number, " is not a Perfect Square")