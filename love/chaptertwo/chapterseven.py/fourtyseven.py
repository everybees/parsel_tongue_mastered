def minimum_value(value):
    minimum = value[0]

    for number in value:
        if number < minimum:
            minimum = number
    return minimum




def maximum_value(value):
    maximum = value[0];

    for number in value:
        if number > maximum:
            maximum = number
    return maximum


if __name__ == '__main__':
    numbers =[int(i) for i in input("enter your numbers:")]

    print(maximum_value(numbers))

    print(minimum_value(numbers))


    