for i in range(10, 100):
    square = i ** 2
    last_two_digit = str(square)[-2:]
    if int(last_two_digit) == i:
        print(i)
        break


