import sys
from pathlib import Path
from itertools import zip_longest
from colorama import Fore, Back, Style
'''
Наш додаток має приймати два файли File1 File2

Він має пройти по рядках цих файлів і знайти рядки які відрізняються

< 1
> a

1. Отримати два шляхи до файлу з терміналу
2. Відкрити ці файли
3. Пройтись по рядках цих файлів та порівняти
'''

# __file__
# print(__file__)

# file_path = Path(__file__)
# print(file_path.parent / 'a.txt')
# print(__name__)
#'/Users/eddielitvinchuk/Documents/Repositories/neoversity-python-core-2025-06-07/2/diff.py'

def main():
    # ['diff.py', 'file_one.txt', 'file_two.txt'][1:]
    # first_file_path = sys.argv[1]
    # second_file_path = sys.argv[2]

    # my_list = ['file_one.txt', 'file_two.txt']
    # _, first_file_path, second_file_path = sys.argv
    # print(first_file_path)
    # print(second_file_path)

    first_file_path, second_file_path = sys.argv[1:]
    print(first_file_path)
    print(second_file_path)

    with open(first_file_path) as file:
        file_one_lines = file.readlines()

    with open(second_file_path) as file:
        file_two_lines = file.readlines()

    print(file_one_lines)
    print(file_two_lines)

    for number, (file_one_line, file_two_line) in enumerate(zip_longest(file_one_lines, file_two_lines)):
        if file_one_line != file_two_line:
            print(number + 1)
            print(f'{Fore.GREEN}<{file_one_line.strip()}{Style.RESET_ALL}')
            print(f'{Fore.RED}>{file_two_line.strip()}{Style.RESET_ALL}')

    # for i in range(len(file_one_lines)):
    #     file_one_line = file_one_lines[i].strip()
    #     file_two_line = file_two_lines[i].strip()

    #     # print(file_one_line)
    #     # print(file_two_line)

    #     if file_one_line != file_two_line:
    #         print(i + 1)
    #         print(f'<{file_one_line}')
    #         print(f'>{file_two_line}')

    # sys.argv

main()