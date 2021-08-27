while True:
    number = int(input())
    sqrt_of_number = number ** 0.5
    if sqrt_of_number.is_integer():
        print(f"{number} is a perfect square.")
        break
    else:
        print(f"{number} is not a perfect square.")
