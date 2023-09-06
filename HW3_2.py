# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

def find_closest_element(list_1, k):
    closest_element = min(list_1, key=lambda x: abs(x - k))
    return closest_element

list_1 = [1, 3, 5, 7, 9]
k = 4
closest_element = find_closest_element(list_1, k)
print(closest_element)
#print("Самый близкий элемент к числу", k, "в массиве", list_1, ":", closest_element)