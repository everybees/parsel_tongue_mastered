def string_list(value):
    list_string = [c for c in value]
    list_string.sort()
    return list_string


if __name__ == '__main__':
    value = input("Enter a word:")
    print(string_list(value))
    name = ""
    for i in string_list(value):
        name += i + ""
    print(name)