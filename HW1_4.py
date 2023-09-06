# Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.

def can_break_chocolate(a, b, c):
    # Проверяем, что c находится в пределах допустимых значений
    if c <= 0 or c >= a * b:
        return "no"

    # Проверяем, что c долек можно разместить в одном из прямоугольников
    if c % a == 0 or c % b == 0:
        return "yes"
    
    return "no"

# Получение входных данных от пользователя
a = 3
b = 2
c = 4

# Проверка возможности отломить шоколадку
result = can_break_chocolate(a, b, c)
print(result)