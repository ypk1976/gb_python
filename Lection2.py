# Lists
# #Empty lists initialization:
# list_1 = []
# list_1 = list()
# # Fill list_1 with values
# list_1 = [1, 5, 6, 89, 2]
# # print(list_1)
# # # Prints list without [] and ,
# # print(*list_1)
# # # Prints length of list
# # print(len(list_1))
# # for i in list_1:
# #     print(i)

# # Access to element of array by address:
# #print(list_1[2])

# #adding elements
# print(list_1)
# list_1.append(274)
# print(list_1)

# # 1
# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# #Element removal
# list_1.pop(0)
# print(list_1)

# #inserting element into array
# list_1.insert(2, 111)
# print(list_1)

# #work with slices
# print(list_1[0])
# print(list_1[len(list_1)-1])
# print(list_1[-2])
# print(list_1[:])
# print(list_1[1:])
# print(list_1[:3])
# print(list_1[1:3])
# print(list_1[::2])

#Tuples (кортежи)
1#
# t = (1,2,4,7,)
# print(type(t))

# list = [7,5,3,1]
# print(list)
# print(type(list))

# list = tuple(list)
# print(list)
# print(type(list))

# a,b,c,d = list
# print(a,b,c,d)

#2
# t = (1,2,3,4,)
# for i in t:
#     print(i)

#Dictionries
# d={}
# d = dict()
# d['q']='qwerty'
# d['w']='123456'
# d[121] = 987765
# print(d)

# dict = {1:12, 2:13,3:345}
# print(dict)

# #element removal
# # del dict[2]
# # print(dict)

# # for i in dict:
# #     #print(i)
# #     print('{}: {}'.format(i,dict[i]))
# print(dict.items())
# for (k,v) in dict.items():
#     print(k,v)

# Sets (множества)
# colors = {'red','blue','green'}
# print(colors)
# colors.add('black')
# print(colors)
# #colors.remove('red')
# #print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

#operations with sets
a = {1,2,3,4,5}
b = {2,7,4,9,1}
# print(a,b)
# c = a.copy()
# print(c)
# d = c.union(b)
# print(d)
# e = a.union(c)
# print(e)
# f = a.intersection(b)
# print(f)
# g = a.difference(b)
# print(g)
# h = b.difference(a) 
# c = a.union(b).difference(a.intersection(b))
# print(c)

#Frozensets
# a = {1,2,3,6,3}
# b = frozenset(a)
# print(b)

#List compehension (генератор списков)
#Вывести четные числа от 1 до 100
# list_1 = [i for i in range(1,101) if i % 2 ==0]
# print(list_1)
# #creating duples
# list_1 = [(i,i) for i in range(1,101) if i % 2 ==0]
# print(list_1)
# making some operations 
# list_1 = [i * 2 for i in range(1,101) if i % 2 ==0]
# print(list_1)
# #making operation with duples
list_1 = [(i,int(i/2)) for i in range(1,101) if i % 2 ==0]
print(list_1)
