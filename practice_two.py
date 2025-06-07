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


