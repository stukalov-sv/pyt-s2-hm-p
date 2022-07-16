# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorials_list(number: int):
    factorial_list = []
    factorial_list.append(1)
    temp_number = 1
    for i in range(1, number):
        temp_number += 1
        factorial_list.append(factorial_list[i-1] * temp_number)
    return factorial_list

user_number = int(input('Enter natural number: '))
print(factorials_list(user_number))

