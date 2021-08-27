import math

sentinel = 0
while sentinel != -1:
    number = int(input("Enter number: "))
    if math.ceil(math.sqrt(number)) == math.floor(math.sqrt(number)):
        print("It is a perfect square")
        sentinel = -1
    else:
        print("Wrong number.Enter number again")
