# Задача No3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

a = int(input("Введите кол-во учеников в первом классе: "))
b = int(input("Введите кол-во учеников во втором классе: "))
c = int(input("Введите кол-во учеников в третьем классе: "))
x = 2
print(f"Учитывая, что за партой сидит {x} учеников, то всего нужно приобрести {round((a+b+c)/x)} парт.")