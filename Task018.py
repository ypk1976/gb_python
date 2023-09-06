# Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8

'''
def find_longest_sequence(numbers):
    max_length = 0
    max_sequence = []
    
    current_length = 1
    current_sequence = [numbers[0]]
    
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:  # Если текущее число больше предыдущего, продолжаем последовательность
            current_length += 1
            current_sequence.append(numbers[i])
        else:
            if current_length > max_length:  # Если текущая последовательность длиннее максимальной, обновляем значения
                max_length = current_length
                max_sequence = current_sequence.copy()
            
            current_length = 1  # Сбрасываем длину и список текущей последовательности
            current_sequence = [numbers[i]]
    
    if current_length > max_length:  # Проверка для последней последовательности в списке
        max_length = current_length
        max_sequence = current_sequence.copy()
    
    return max_sequence

# Пример использования
numbers = [1, 5, 2, 3, 4, 6, 1, 7]  # Пример входного списка чисел
longest_sequence = find_longest_sequence(numbers)
print("Максимальная возрастающая последовательность:", longest_sequence)
'''
