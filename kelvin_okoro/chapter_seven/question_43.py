# Write a function that takes a string as an argument, converts the string to a list of
# characters, sorts the list, converts the list back to a string, and returns the resulting string.


def conversion(strings, ):
    my_list = []
    my_list += strings
    my_list.sort()
    my_new_string = ""
    return my_new_string.join(my_list)


my_love = "Lordship"
print(conversion(my_love))
