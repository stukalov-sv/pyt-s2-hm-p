# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def float_digit_sum(number) -> int:
    amount = 0
    for i in range(0, len(number)):
        if(number[i] != ','):
            amount += int(number[i])
        else:
            i += 1
    return amount

user_number = str(input('Enter real number with comma: '))
print(float_digit_sum(user_number))
