# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции

def get_binary_octal_representation(num: int) -> str:
    binary = bin(num)[2:]
    octal = oct(num)[2:]
    return binary, octal

# Ввод целого числа от пользователя
num = int(input("Введите целое число: "))

# Получение двоичного и восьмеричного представления числа
binary, octal = get_binary_octal_representation(num)

# Вывод результата
print("Двоичное представление:", binary)
print("Восьмеричное представление:", octal)