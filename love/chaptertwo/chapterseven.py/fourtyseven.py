def minimum_value(value):
    minimum = 0;
    temp = 0;

    for _ in value:
        if value[0] > minimum:
           temp = value[0]

        if _ < temp:
            minimum = _
        else:
            minimum = temp

    return minimum




def maximum_value(value):
    maximum = 0;
    temp = 0;

    for _ in value:
        if value[0] > maximum:
           temp = value[0]

        if _ > temp:
            maximum = _
        else:
            maximum = temp

    return maximum


if __name__ == '__main__':
    numbers =[int(i) for i in input("enter your numbers:")]

    print(maximum_value(numbers))

    print(minimum_value(numbers))


    