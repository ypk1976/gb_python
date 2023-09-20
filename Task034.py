# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 

def check_rhythm(poem):
    lines = poem.split()
    vowel_counts = []

    for line in lines:
        words = line.split("-")
        count = sum(count_vowels(word) for word in words)
        vowel_counts.append(count)

    if vowel_counts.count(vowel_counts[0]) == len(vowel_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"

def count_vowels(word):
    vowels = "aeiouаеёиоуыэюя"
    count = 0

    for letter in word:
        if letter.lower() in vowels:
            count += 1

    return count

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)