for i in range(10, 100):
    square: int = i * i
    list_number: list = [j for j in str(square)]
    if len(list_number) == 3:
        if (int(list_number[1]) * 10) + int(list_number[2]) == i:
            print(i)
    if len(list_number) == 4:
        if (int(list_number[2]) * 10) + int(list_number[3]) == i:
            print(i)
