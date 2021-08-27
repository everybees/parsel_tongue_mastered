char_list = input("Enter a string")
container = [char for char in char_list]
container.sort()
print("".join(container))
