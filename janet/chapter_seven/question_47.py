def max_number(lists):
    maximum = lists[0]
    minimum = lists[0]
    for i in range(len(lists)):
        if lists[i] > maximum:
            maximum = lists[i]
        if lists[i] < minimum:
            minimum = lists[i]

    print("The maximum number is ", maximum)
    print("The minimum number is ", minimum)


print(max_number([65,73,91,26,92,100,150]))
