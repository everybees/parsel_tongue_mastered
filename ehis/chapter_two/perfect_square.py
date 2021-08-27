def is_perfect_square():
    number: int = int(input("Enter a number: "))

    if (number ** 0.5).is_integer():
        print(number, "is a perfect square")
    else:
        is_perfect_square()


if __name__ == "__main__":
    is_perfect_square()
