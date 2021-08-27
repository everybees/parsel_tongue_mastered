def max_number(lists):
    maximum = lists[0]
    for i in range(len(lists)):
        if lists[i] > maximum:
            maximum = lists[i]
    return maximum


def min_number(lists):
    minimum = lists[0]
    for i in range(len(lists)):
        if lists[i] < minimum:
            minimum = lists[i]

    return minimum


print("The maximum number is ", max_number([65, 73, 91, 26, 92, 100, 150]))
print("The minimum number is ", min_number([65, 73, 91, 26, 92, 100, 150]))
