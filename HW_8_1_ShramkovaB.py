def add_one(some_list): 
    my_variable = str()
    result = list()

    for i in some_list:
        my_variable += str(i)

    my_int_plus_one = int(my_variable) + 1

    for k in str(my_int_plus_one):
        result.append(int(k))

    return result

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1' 
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2' 
assert add_one([0]) == [1], 'Test3' 
assert add_one([9]) == [1, 0], 'Test4' 
print("OK")
