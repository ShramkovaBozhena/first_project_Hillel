def generate_cube_numbers(end):
    for i in range(2, end):
        cube = i ** 3
        if cube <= end:
            yield cube
        else:
            return

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'Test1'
assert list(generate_cube_numbers(100)) == [8, 27, 64], 'Test2' 
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000],'Test3'
print('Ok') 