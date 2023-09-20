# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.
# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

import random

def generate_polynomial(k):
    polynomial = ""

    for i in range(k+1):
        coefficient = random.randint(-10, 10)
        
        if coefficient != 0:
            power = k - i
            term = str(coefficient) + "*x^" + str(power)
            polynomial += term

            if i != k:
                polynomial += " + "
    
    return polynomial + " = 0"

k = int(input("Введите степень многочлена: "))

polynomial = generate_polynomial(k)
print(f"{k} -> {polynomial}", )