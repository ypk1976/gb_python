# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 
def is_fibonacci_number(A):
    fibonacci_numbers = [0, 1]
    
    # Генерируем числа Фибоначчи, пока не достигнем A или превысим его
    while fibonacci_numbers[-1] < A:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    
    if fibonacci_numbers[-1] == A:  # Если последний элемент списка равен A, то A является числом Фибоначчи
        return True
    else:
        return False

def find_fibonacci_position(A):
    fibonacci_numbers = [0, 1]
    position = 2
    
    # Генерируем числа Фибоначчи, пока не найдем число A или превысим его
    while fibonacci_numbers[-1] < A:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
        position += 1
    
    if fibonacci_numbers[-1] == A:  # Если последний элемент списка равен A, возвращаем позицию числа A в последовательности Фибоначчи
        return position
    else:
        return -1  # Если A не является числом Фибоначчи, возвращаем -1

# Пример использования
A = int(input("Введите число A: "))  # Пример ввода числа с клавиатуры
if is_fibonacci_number(A):
    position = find_fibonacci_position(A)
    print("Число {} является {}-м числом Фибоначчи.".format(A, position))
else:
    print("Число {} не является числом Фибоначчи.".format(A))