import math

# number = int(input('Enter a number'))
# root = math.sqrt(number)
# if int(root + 0.5) ** 2 == number:
#     print('Number is  perfect square')
# else:
#     print('number is not perfect square')

while(True):
    number = int(input('Enter a number to match: '))
    square_root = int(number ** 0.5)
    if square_root * square_root == number:
        print('is a perfect square number')
        break
    else:
        print('number is not a perfect square')