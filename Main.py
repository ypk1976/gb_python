# print("Hello, world!")
# print(5)

# #Вывод типа переменной
# n = 5
# m = 'hello!'
# print(type(m))

# # Примеры интерполляции
# a = 2
# b = 3.14
# c = 'hello'
# print(a,'-', b,'-', c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

# # Ввод данных
# print('Введите что-то')
# a = input()
# print(f"Вы ввели '{a}'")
# b = input('Введите еще что-то: ')
# print(f"Вы ввели '{b}'")


# # Приведение типов
# # 1
# a = int(input('Введите 1-е число: '))
# b = int(input('Введите 2-е число: '))
# print("a + b = ", a + b)
# # 2
# # c = 3.678
# # print(c)
# # n = int(c)
# # print(n)

# Округление чисел (round(число, кол-во знаков после запятой))
# a = 3.2134
# b = 6.22567
# print(a * b)
# print(round(a * b,3))


# # Циклы
# # 1
# # a = 'whatever'
# # print(a[0])
# # for i in a:
# #     print(i)

# # 2
# # line = ''
# # for i in range(5):
# #     line = ''
# #     for j in range(5):
# #         line += '1'
# #         print(line)

# # Работа со строками
# text = 'Founded in 14th century BC by Pharaoh Smenkhkare in ancient Egypt.'
# # print(len(text))
# # print('by' in text)
# # print(text.upper())
# # print(text.lower())
# # print(text.replace('by', 'bloody hell'))
# print(text[:])
# print(text[:5])
# print(text[5:])
# print(text[5:-5])

# # Работа с условиями
# username = input("Enter your name: ")
# if username == 'Mitya':
#     print(f"Hi, {username}")
# elif username == 'Nina':
#     print(f"Hello, {username}")
# else:
#     print(f"Who is {username}?")

# Циклы
# #1
# n=4327
# summa = 0
# while n > 0:
#     x=n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)

# #2
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
#     print(f"i= {i}")
# else:
#     print("Enough")
# print(f"final i= {i}")

#3 работа с флагами
# n = int(input("Enter some N: "))
# flag = True
# i = 2
# while flag == True:
#     if n % i == 0:
#         flag = False
#         print(f"Divider is: {i}")
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1
    
# Цикл for
# #1
# a = 'qwerty'
# for i in a:
#     print(i)

#2
# line = ""
# for i in range(6):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)
# PRACTICE 2
#list = [123, 'whatever', 5672, True, [432, 'dexterity', 'sex, drugs & rocknroll', 589.54], False]
# for i in range(len(list)):
#     print(list[i], end = '\n')

# for new in list:
#     print(new, end = ' ')

# for item in enumerate(list):
#     print(item)

#Functions  
from random import *
from time import *

def some_test(low_limit: int, high_limit: int) -> str:
    print(randint(low_limit,high_limit))


print(some_test(1,100))
#print(time,time())
