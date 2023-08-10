# Задача 2: Найдите сумму цифр трехзначного числа.

num = int(input("Enter three-digit number: "))
if num > 99 and num < 1000:
    sum = 0
    while num > 9:
        sum += num % 10
        num //= 10
    sum += num
    print("Sum of digits = ", sum)
else:
    print("Wrong number")