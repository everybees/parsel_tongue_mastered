def find_min(array):
    minimum = array[0]
    for x in range(len(array)):
        if minimum < array[x]:
            minimum = array[x]
    print('minimum = ', minimum)


def find_max(array):
    maximum = array[0]
    for x in range(len(array)):
        if maximum > array[x]:
            maximum = array[x]
    print('maximum = ', maximum)


find_min([5, 10, 100, 49, 2])
find_max([5, 10, 100, 49, 2])
