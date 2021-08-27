import math

while(True):
    number = int(input("Enter a number: "))

    # square_root = int(number ** 0.5)

    # if square_root * square_root == number:
    #     print(f"the number {number} is a perfect square")
    #     break
    # else:
    #     print(f"the number {number} is not a perfect square, try another number")

    square_root = math.sqrt(number)
    print(square_root)

    if square_root.is_integer():
        print(f"the number {number} is a perfect square")
        break
    else:
        print(f"the number {number} is not a perfect square, try another number")
