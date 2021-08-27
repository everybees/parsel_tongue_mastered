for i in range(10, 100):
    square: int = i * i
    if square > 999:
        continue
    list_number: list = [j for j in str(square)]
    if (int(list_number[1]) * 10) + int(list_number[2]) == i:
        print(i)
