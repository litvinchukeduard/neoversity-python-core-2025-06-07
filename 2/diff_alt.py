import sys
from pathlib import Path
from itertools import zip_longest
from colorama import Fore, Back, Style

def main():
    first_file_path, second_file_path = sys.argv[1:]
    with open(first_file_path) as file_one:
        with open(second_file_path) as file_two:
            number = 0
            while True:
                file_one_line = file_one.readline()
                file_two_line = file_two.readline()

                # if file_one_line is not None # !=

                if not file_one_line and not file_two_line:
                    break

                if file_one_line != file_two_line:
                    print(number + 1)
                    print(f'{Fore.GREEN}<{file_one_line.strip()}{Style.RESET_ALL}')
                    print(f'{Fore.RED}>{file_two_line.strip()}{Style.RESET_ALL}')

                number += 1
main()