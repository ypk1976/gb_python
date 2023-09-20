# Даны два многочлена, которые вводит пользователь как две строки.
# Задача - сформировать многочлен, содержащий сумму многочленов, и вывести как строку.
# Степени многочленов могут быть разные.
# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re

import re

def sum_polynomials(poly1, poly2):
    terms1 = re.findall(r'([+-]?\d*)\*?x\^(\d+)', poly1)
    terms1 = [(int(coef), int(power)) for coef, power in terms1]

    terms2 = re.findall(r'([+-]?\d*)\*?x\^(\d+)', poly2)
    terms2 = [(int(coef), int(power)) for coef, power in terms2]

    coefficients_sum = {}

    for coef, power in terms1:
        if power in coefficients_sum:
            coefficients_sum[power] += coef
        else:
            coefficients_sum[power] = coef

    for coef, power in terms2:
        if power in coefficients_sum:
            coefficients_sum[power] += coef
        else:
            coefficients_sum[power] = coef

    sum_polynomial = ""
    for power in coefficients_sum:
        coef = coefficients_sum[power]
        if power == 0:
            term = f"{coef}"
        elif power == 1:
            term = f"{coef}*x"
        else:
            term = f"{coef}*x^{power}"
        
        if coef >= 0:
            term = "+" + term

        sum_polynomial += term

    if sum_polynomial == "":
        sum_polynomial = "0"
    
    return sum_polynomial + " = 0"

poly1 = input("Введите первый многочлен: ")
poly2 = input("Введите второй многочлен: ")

sum_poly = sum_polynomials(poly1, poly2)
print("Многочлен суммы:", sum_poly)