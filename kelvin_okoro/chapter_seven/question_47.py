# Write your own versions of the Python built-in functions min and max. They should
# take a list as an argument and return the minimum or maximum element. Hint: Pick
# the first element as the minimum (maximum) and then loop through the elements to
# find a smaller (larger) element. Each time you find a smaller (larger) element, update
# your minimum (maximum).


my_list = [1, 2, 3, 4, 5, 7]


def minimum(my_method):
    min_num = my_method[0]
    for num in range(len(my_method)):
        if my_method[num] < min_num:
            min_num = my_method[num]
    return min_num


print(minimum(my_list))


def maximum(my_method):
    max_num = my_method[0]
    for num in range(len(my_method)):
        if my_list[num] > max_num:
            max_num = my_method[num]
    return max_num


print(maximum(my_list))

