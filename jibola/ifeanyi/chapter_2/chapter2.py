import math

number = int(input('Enter a number '))
perfect_square = math.sqrt(number) ** 2
if perfect_square == number:
    print('Its a perfect square')
else:
    print('Not a perfect square')