def common_elements():
    my_set_one = set(range(0, 100, 3))
    my_set_two = set(range(0, 100, 5))
    result = my_set_one.intersection(my_set_two)
    return result

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, "Test1"
print("OK")



