my_list = [10, 12, 3, 4]


if len(my_list) > 1:
    last_numb = [my_list[-1]]
    my_list.pop()
    new_list = last_numb + my_list
    print(new_list)
else:
    print(my_list)

