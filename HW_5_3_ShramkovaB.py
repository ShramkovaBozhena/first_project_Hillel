import string

my_str = input("Enter your sentence for a hashtag: ")

new_str = my_str.title()
symbol = string.punctuation + " "

for i in symbol:
    new_str = new_str.replace(i, "")

new_str = "#" + new_str[0:138]

print(new_str)