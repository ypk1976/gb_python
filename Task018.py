# Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную сплошную возрастающую 
# последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8

def find_longest_sequence(numbers):
    max_length = 0
    max_sequence = []
    final_result = []
    
    current_length = 1
    current_sequence = [numbers[0]]
    
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            current_length += 1
            current_sequence.append(numbers[i])
        else:
            if current_length > max_length:
                max_length = current_length
                max_sequence = current_sequence.copy()
                final_result = [max_sequence[0],(max_sequence[len(max_sequence)-1])]
            
            current_length = 1
            current_sequence = [numbers[i]]
    
    if current_length > max_length:
        max_length = current_length
        max_sequence = current_sequence.copy()
        final_result = [max_sequence[0],(max_sequence[len(max_sequence)-1])]
    
    return final_result

numbers = [1, 5, 2, 3, 4, 6, 1, 7]
longest_sequence = find_longest_sequence(numbers)
print(f"{numbers} => {longest_sequence}")

