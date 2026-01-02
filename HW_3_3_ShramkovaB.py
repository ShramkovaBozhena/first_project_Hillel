my_list = [1, 2, 3, 4, 5, 6]
len_list = len(my_list)

if my_list == [] or len_list == 1:
    print([my_list] + [[]])

elif len_list % 2 == 0:
    md_index = int(len_list / 2)
    my_new_list = [my_list[:md_index]] + [my_list[-md_index:]]
    print(my_new_list)

else:
    md_index = int(len_list/2)
    print([my_list[:md_index + 1]] + [my_list[-md_index:]])
