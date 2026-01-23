def add_one(some_list): 
    copy_some_list = some_list[::-1]
    for idx, item in enumerate(copy_some_list):
        if item < 9:
            copy_some_list[idx] += 1
            break
            
        else:
            copy_some_list[idx] = 0
            if idx == len(copy_some_list) - 1:
                copy_some_list.append(1)
                break
    return copy_some_list[::-1]

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1' 
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2' 
assert add_one([0]) == [1], 'Test3' 
assert add_one([9]) == [1, 0], 'Test4' 
print("OK")