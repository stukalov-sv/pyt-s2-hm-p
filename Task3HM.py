# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.
#
# *Пример:*
#
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037,
# 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}


def equations_list(number: int) -> list:
    equation_list = []
    for i in range(1, number+1):
        equation_list.append((1+1/i)**i)
    return equation_list


def list_amount(user_list: list) -> float:
    result = 0
    for i in range(0, len(user_list)):
        result += user_list[i]
    return result


user_number = int(input('Enter natural number: '))
print(equations_list(user_number))
amount = round(list_amount(equations_list(user_number)), 2)
print(f'List elements amount -> {amount}')
