# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

def count_repeats(list_1,k):
    count = 0
    for i in list_1:
        #print(i)
        if i == k:
            count+=1
    return count
            
        
    
list_1 = [1, 1, 3, 4, 5]
k = 1
result = count_repeats(list_1,k)
print(f"Число k встречается {result} раз")