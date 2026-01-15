my_str = input("Enter your number: ")
result = int(my_str)

while result > 9:
    my_list = [int(k) for k in str(result)]
    my_variable = 1

    for k in my_list:
        my_variable *= k

    result = my_variable

print(result)
