# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

def find_indexes(lst, min_val, max_val):
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return indexes

lst = [random.randint(0, 100) for _ in range(10)]
#lst = [1, 5, 88, 100, 2, -4]
print("На входе:", lst)

min_val = int(input("Введите минимальное значение диапазона: "))
max_val = int(input("Введите максимальное значение диапазона: "))

indexes = find_indexes(lst, min_val, max_val)
print("Ответ:", indexes)