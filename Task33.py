# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def negafibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 0:
        return negafibonacci(n - 2) - negafibonacci(n - 1)
    elif n < 0:
        return negafibonacci(n + 2) + negafibonacci(n + 1)

k = int(input("Введите число k: "))

fibonacci_list = [negafibonacci(i)*-1 for i in range(-abs(k), abs(k) + 1)]
print("Список чисел Фибоначчи (включая отрицательные индексы):", fibonacci_list)