'''
Потрібно написати код, який допоможе керувати бюджетом

$100

Вводимо бюджет на тиждень

Вводимо витрати на денб
'''

DAYS_OF_THE_WEEK = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
)

def get_number_from_user_with_prompt(prompt, default_value):
    try:
        number = int(input(prompt))
    except ValueError:
        print("Number value is not correct. We are setting budget to 100...")
        number = default_value

    return number

weekly_budget = get_number_from_user_with_prompt("Enter weekly budget", 100)
print(weekly_budget + 100)

expenses = []
for day in DAYS_OF_THE_WEEK:
    expenses.append(get_number_from_user_with_prompt("Enter " + day + " expenses: ", 100))

# sum([1, 2, 3, 4])

# sum = 0
# list = []

sum_of_expenses = 0
for expense in expenses:
    sum_of_expenses += expense

expenses_difference = weekly_budget - sum_of_expenses
print("Total expenses: " + str(sum_of_expenses))
print("Difference: " + str(expenses_difference))

# max_expense = max(expenses)
# print(max_expense)

# enumerate

max_index = 0
max_expense = 0
for i in range(len(expenses)):
    expense = expenses[i]
    if expense > max_expense:
        max_index = i
        max_expense = expense

print("On " + DAYS_OF_THE_WEEK[max_index] + " you spent " + str(max_expense))
