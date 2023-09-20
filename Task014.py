# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

def powers_of_two(N):
    k = 0
    power_of_two = 1
    while power_of_two <= N:
        print(power_of_two)
        k += 1
        power_of_two = 2 ** k

N = 20
powers_of_two(N)
