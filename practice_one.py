'''
Потрібно написати код, який допоможе керувати бюджетом

$100

Вводимо бюджет на тиждень

Вводимо витрати на денб
'''

# Hello world

# First step: Enter budget
# weekly_budget = input("Enter budget for the week: ")
# print(weekly_budget)

#hello 
# First step: Enter budget

# Dummy change

# Ctrl /
# COMMAND /
# weekly_budget = input("Enter budget for the week :") # not int, but str "100.16" "100"
# weekly_budget = int(weekly_budget)

def get_number_from_user():
    try:
        number = int(input("Enter number: "))
    except ValueError:
        print("Number value is not correct. We are setting budget to 100...")
        number = 100

    return number

def get_number_from_user_with_prompt(prompt, default_value):
    try:
        number = int(input(prompt))
    except ValueError:
        print("Number value is not correct. We are setting budget to 100...")
        number = default_value

    return number

# try:
#     weekly_budget = int(input("Enter budget for the week :")) # not int, but str "100.16" "100"
# except ValueError:
#     print("Weekly budget value is not correct. We are setting budget to 100...")
#     weekly_budget = 100

print("Enter weekly budget")
weekly_budget = get_number_from_user()
print(weekly_budget + 100)

expenses = []

# Monday -> 
# Tuesday -> 
# Wednesday ->

# list, set, dict, tuple

# list: expenses = [100, 200, 300]
# monday_expenses = expenses[0]

# set: expenses = {100, 200, 300} -> {300, 200, 100} | Do not recommend

# dict: expenses = {'Monday': 100, 'Tuesday': 200, 'Wednesday': 300}

# tuple: (1, 2, 3) Unchangeable -> No recommended 

# days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_of_the_week = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
)

# for i in range(0, 7):
#     # print(days_of_the_week[i])
#     day = days_of_the_week[i]
#     expenses.append(get_number_from_user_with_prompt("Enter " + day + " expenses: ", 100))

for day in days_of_the_week:
    expenses.append(get_number_from_user_with_prompt("Enter " + day + " expenses: ", 100))

# # Витрати на Понеділок
# expenses.append(get_number_from_user_with_prompt("Enter Monday expenses: ", 100))

# # Витрати на Вівторок
# expenses.append(get_number_from_user_with_prompt("Enter Tuesday expenses: ", 200))

# # Витрати на Середу
# expenses.append(get_number_from_user_with_prompt("Enter Wednesday expenses: ", 300))

# print(expenses)


# '300a'

