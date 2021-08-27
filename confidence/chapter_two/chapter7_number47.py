def minimum(num_lists):
    min_num =num_lists[0]
    for i in range (len(num_lists)):
        if num_lists[i] < min_num:
            min_num = num_lists[i]
    print(min_num, " is the Minimum number")
minimum([20,50,49,87,23,56,8,90,23,44,56])

def maximum(num_lists):
    max_num =num_lists[0]
    for i in range (len(num_lists)):
        if num_lists[i] > max_num:
            max_num = num_lists[i]
    print(max_num, " is the Maximum Number")

maximum([20,50,49,87,23,56,8,90,23,44,56])