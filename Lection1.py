num = int(input("Введите какое-то число: "))
# i=0
# while i <= num:
#     print(f"Квадрат числа {i} равен {i **2}")
#     i+=1

for i in range(num+1):
    print(f"Квадрат числа {i} равен {i **2}")
    if i % 2 == 1:
        print(f"Нечетное число - {i}")
