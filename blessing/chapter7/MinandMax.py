def _min(number):
    min_value = 0
    for i in number:
        if i < min_value:
            min_value = i
    return min_value


def _max(number):
    max_value = 0
    for i in number:
        if i > max_value:
            max_value = i
    return max_value


print(_min([232]))

print(_max([23]))


