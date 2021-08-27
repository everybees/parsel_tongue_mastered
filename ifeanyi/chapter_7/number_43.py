def manipulate_string(value):
    array = [x for x in value]
    list.sort(array)
    new_string = ''.join(array)
    print(new_string)


manipulate_string('Coming')
