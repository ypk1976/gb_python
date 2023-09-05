# Задача 2: Найдите сумму цифр трехзначного числа.

n = int(input("Enter three-digit number: "))
res = 0
while n > 9:
    res += n % 10
    n //= 10
res = res + n
print("res of digits = ", res)
