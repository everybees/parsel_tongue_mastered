import math

three_digit_list = []

for i in range(10, 32):
    three_digit = i ** 2
    three_digit_list.append(three_digit)
    
for number in three_digit_list:
    squre_root = math.sqrt(number)
    if number % 100 == squre_root:
        print(squre_root)