import sys
'''
Потрібно зробити інструмент, який працює схоже до cat в терміналі

cat 1/main.py

python3 2/first.py 1/main.py
'''

# print(sys.argv[1])

# 1. Отримати шлях до файлу

# str
# int

# def main

if len(sys.argv) != 2:
    print("Please provide file path")
    exit(1)

file_path = sys.argv[1]

# 2. Відкрити файл
with open(file_path, 'r') as file:
    # 3. Вивести все що є в файлі
    for line in file:
        # print(line.strip())
        print(line, end='')





