from functools import reduce
'''
Написати систему, яка буде керувати піснями та плейлістами

Потрібно зберігати інформацію про пісню (автор, назва, довжина (сек), жанр)

Плейліст (Коллекція пісень)

Playlist(UserList)
'''

my_list = [1, 2, 3, 4]

print(reduce(lambda accumulator, element: accumulator + element, my_list))
