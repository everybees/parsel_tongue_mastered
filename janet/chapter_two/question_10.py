import math

number = int(input("Enter a number: "))

print(math.isqrt(number))
square = (math.isqrt(number)) ** 2
if square == number:
    print("It is a perfect square")

else:
    print("It is not a perfect square")
