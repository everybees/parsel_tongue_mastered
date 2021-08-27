import math

three_digit_list = []

for i in range(10, 32):
    three_digit = i ** 2
    three_digit_list.append(str(three_digit))
    
for number in three_digit_list:
    number_int = int(number)
    squre_root = math.sqrt(number_int)
    compare = number[1] + number[2]
    if int(compare) == squre_root:
        print(squre_root)
    
# print(three_digit_list)