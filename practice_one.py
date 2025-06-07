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
        weekly_budget = int(input("Enter budget for the week :"))
    except ValueError:
        print("Weekly budget value is not correct. We are setting budget to 100...")
        weekly_budget = 100

    return weekly_budget

# try:
#     weekly_budget = int(input("Enter budget for the week :")) # not int, but str "100.16" "100"
# except ValueError:
#     print("Weekly budget value is not correct. We are setting budget to 100...")
#     weekly_budget = 100

weekly_budget = get_number_from_user()
print(weekly_budget + 100)

# Витрати на Понеділок



# '300a'

