for i in range(10, 100):
    squaredDigit = i ** 2
    last_two_digits = str(squaredDigit)[-2:]
    if int(last_two_digits) == i:
        print(i)