# Реализуйте алгоритм перемешивания списка.

import time

def list_create(number: int) -> list:
    user_list = []
    for i in range(0, number):
        user_list.append(i)
        i += 1
    return user_list

def init_shuffle(user_list_length: int) -> list:
    message = input('\nPress "Enter" to start shuffle: ')
    active = True
    start = time.perf_counter_ns()

    while (active):
        message = input('\nStart shuffling. Enter "stop" to end shuffle: ')

        if (message == 'stop'):
            active = False
            finish = time.perf_counter_ns()
            duration = (finish - start)//100

    first_temp_list = []

    while duration > 0:
        first_temp_list.append(duration % 10)
        duration //= 10

    if (user_list_length <= 9):
        for i in range(0, len(first_temp_list)):
            if (first_temp_list[i] >= user_list_length >= 5):
                first_temp_list[i] = first_temp_list[i] - user_list_length
                i += 1
            elif (first_temp_list[i] >= user_list_length == 4):
                first_temp_list[i] = abs(first_temp_list[i] - 6)
                i += 1

    result_index_list = []
    [result_index_list.append(i) for i in first_temp_list if i not in result_index_list]

    if (len(result_index_list) < user_list_length):
        temp_list = []
        model_list = sorted(range(0, user_list_length))
        for i in model_list:
            if (i not in result_index_list):
                temp_list.append(i)

    temp_index = len(result_index_list)

    for i in range(len(result_index_list), user_list_length):
        result_index_list.append(temp_list[i - temp_index])
        i += 1

    return (result_index_list)

def list_shuffle(user_list: list, random_index_list: list) -> list:
    for i in range(0, len(user_list)-1):
        temp_number = user_list[i]
        user_list[i] = user_list[random_index_list[i]]
        user_list[random_index_list[i]] = temp_number
        i += 1
    return user_list


user_number = int(input('Enter length of shuffled numbers list >= 4: '))
user_list = list_create(user_number)

new_index_list = init_shuffle(len(list_create(user_number)))

print('\nUnshuffled list:')
print(user_list)
print('\nShuffled list:')
print(list_shuffle(user_list, new_index_list))
