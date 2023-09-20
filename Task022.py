# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

def find_common_elements(n, m, set1, set2):
    set1 = set(set1)
    set2 = set(set2)

    common_elements = set1.intersection(set2)

    sorted_elements = sorted(common_elements)

    return sorted_elements

n = int(input("Введите количество элементов первого множества: "))
set1 = []
for i in range(n):
    element = int(input("Введите элемент множества 1: "))
    set1.append(element)

m = int(input("Введите количество элементов второго множества: "))
set2 = []
for i in range(m):
    element = int(input("Введите элемент множества 2: "))
    set2.append(element)

result = find_common_elements(n, m, set1, set2)
print("Общие элементы, в порядке возрастания:", result)