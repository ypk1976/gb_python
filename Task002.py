# Задача 2: Найдите сумму цифр трехзначного числа.

<<<<<<< HEAD
n = int(input("Enter three-digit number: "))
res = 0
while n > 9:
    res += n % 10
    n //= 10
res = res + n
print("res of digits = ", res)
=======
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
>>>>>>> a1868c81e027ee89d880ab863a1eef15079ce3e8
