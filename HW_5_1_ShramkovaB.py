import string
import keyword

my_str = input("Enter your variable name: ")

my_bool_result = True
only_letters = ""

for i in my_str:
    if i.isalpha():
        only_letters += i

upper_str = only_letters.upper()
symbols_and_upper = string.punctuation.replace("_", " ") + upper_str

for k in symbols_and_upper:
    if k in my_str:
        my_bool_result = False
        break

if my_str[0].isdigit():
    my_bool_result = False

if my_str in keyword.kwlist:
    my_bool_result = False

if '__' in my_str:
    my_bool_result = False

print(my_bool_result)
