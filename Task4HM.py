# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции вводит пользователь через пробел.

def list_create(number: int) -> list:
    temp_number = -number
    result_list = []
    for i in range((number * 2) + 1):
        result_list.append(temp_number)
        temp_number += 1
    return result_list

def convert_str_to_int_list(user_string: str) -> list:
    temp_list = list(user_string.split())
    result_list = list(map(int, temp_list))
    return result_list

def list_elements_multiply(user_list: list, user_indexes_list: list) -> int:
    multiply = 1
    for i in range(len(user_list)):
        for j in range(len(user_indexes_list)):
            if (i == user_indexes_list[j]):
                multiply *= user_list[i]
    return multiply

user_number = int(input('Enter natural number: '))
user_list = list_create(user_number)
print(user_list)

user_indexes = str(input('Enter indexes of elements to multiply with space: '))
result_index_list = convert_str_to_int_list(user_indexes)

if (max(result_index_list) < len(user_list)):
    result_index_list.sort()
    print(f'Indexes to multiply: {result_index_list}')

    multiply = list_elements_multiply(user_list, result_index_list)
    print(multiply)
else:
    print('Incorrect indexes')
