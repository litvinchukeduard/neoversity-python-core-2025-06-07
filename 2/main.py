from itertools import zip_longest

my_list_one = ['a', 'b', 'c', 'd', 'e', 'f']
my_list_two = ['x', 'y', 'z']

# zip
# for pair in zip(my_list_one, my_list_two):
#     print(pair)

for i, (first_list_element, second_list_element) in enumerate(zip_longest(my_list_one, my_list_two, fillvalue='-')):
    print(i)
    print(first_list_element, second_list_element)


# print()
