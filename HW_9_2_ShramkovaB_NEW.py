def difference(*args):
    if not args:
        return 0
    
    min_numb = max_numb = args[0]

    for numb in args:
        if numb < min_numb:
            min_numb = numb
        if numb > max_numb:
            max_numb = numb
            
    result = round((max_numb - min_numb), 2)
    return result

assert difference(1, 2, 3) == 2, 'Test1' 
assert difference(5, -5) == 10, 'Test2' 
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3' 
assert difference() == 0, 'Test4' 
print('OK')

