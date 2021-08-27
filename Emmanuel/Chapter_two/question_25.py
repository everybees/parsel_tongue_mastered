
import math
nuel_loop = True
number = 9
found = 0

while nuel_loop and number < 99:
    number += 1

    square = int(number) ** 2
    #print(str(number) + " | " + str(square)[-2] + str(square)[-1])

    if str(number) == str(square)[-2] + str(square)[-1]:
        found += 1
        print(str(number) + " = " + str(square))
else:
    if found == 0:
        print("Their are no numbers possible in the form AB * AB = CAB")