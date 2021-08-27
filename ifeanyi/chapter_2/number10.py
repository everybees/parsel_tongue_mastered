import math


def is_perfect_number():
    number = int(input('Enter a number '))
    perfect_square = int(math.sqrt(number)) ** 2
    if perfect_square == number:
        return True
    else:
        return False


while True:
    if is_perfect_number():
        print('Its a perfect number')
        break
    else:
        print('Its not a perfect number')
        is_perfect_number()
        if True:
            print('Its a perfect number')
            break