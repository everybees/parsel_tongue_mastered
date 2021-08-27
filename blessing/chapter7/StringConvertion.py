def string_convert(convert):
    x = [i for i in convert]
    list.sort(x)
    new_str = ''.join(x)
    print(new_str)


if __name__ == '__main__':
    string_convert('hello')
