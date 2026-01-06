import random
random_len_list = random.randint(3, 10)
my_list = []
i = 0

while i < random_len_list:
    my_list.append(random.randint(0, 9))
    i = i + 1

print(my_list)

my_new_list = [my_list[0], my_list[2], my_list[-2]]

print(my_new_list)
