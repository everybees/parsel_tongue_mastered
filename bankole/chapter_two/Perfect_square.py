number = int(input("Enter a number: "))

square_root = number ** 0.5

while int(square_root + 0.5) ** 2 != number:
    number = int(input("Not a perfect square, input again"))

if int(square_root + 0.5) ** 2 == number:
     print(number, "is a perfect square")



