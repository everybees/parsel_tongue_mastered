#sample ---> Number AB = AB * AB = CAB for some C

for i in range(10, 100):
    square = i ** 2
    last_two_digits = str(square)[-2:]
    if int(last_two_digits) == i:
        print(i)
        break
