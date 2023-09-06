# Напишите программу, которая принимает на вход целое или дробное число и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4

'''
def count_digits(number):
    number_str = str(number)  # Преобразуем число в строку
    if '.' in number_str:  # Проверяем, является ли число дробным
        digits = len(number_str) - 1  # Вычитаем 1, чтобы исключить точку из подсчета
    else:
        digits = len(number_str)
    return digits

# Пример использования
number = float(input("Введите число: "))  # Пример ввода числа с клавиатуры
digit_count = count_digits(number)
print("Количество цифр в числе:", digit_count)
'''