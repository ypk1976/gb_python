# Напишите программу, которая принимает на вход целое или дробное число и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4

def count_digits(number):
    number_str = str(number)
    if '.' or ',' in number_str:
        digits = len(number_str) - 1
    else:
        digits = len(number_str)
    return digits

number = input("Введите число: ")
digit_count = count_digits(number)
print(f"{number} -> {digit_count}")
