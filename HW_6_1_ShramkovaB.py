import string

my_letters = input("Enter two letters separated by a hyphen: ")
import_letters = string.ascii_letters

first_index = my_letters[0]
last_index = my_letters[-1]

result = import_letters[import_letters.find(first_index):(import_letters.find(last_index) + 1)]

print(result)