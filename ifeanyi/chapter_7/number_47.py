def find_min_max(array):
    minimum = array[0]
    maximum = array[0]
    for x in range(len(array)):
        if minimum < array[x]:
            minimum = array[x]
        if maximum > array[x]:
            maximum = array[x]
    print('minimum = ', minimum, 'maximum = ', maximum)


find_min_max([5, 10, 100, 49, 34])
