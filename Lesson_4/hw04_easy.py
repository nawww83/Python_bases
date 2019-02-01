# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [0, 1, 2, 3] --> [0, 1, 4, 9]

listA = [0, 1, 2, 3]

listB = [el**2 for el in listA]

print(listB)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

listA = ['banana', 'apple', 'qiwi', 'lemon']
listB = ['orange', 'pineapple', 'apple', 'durian', 'qiwi']

listC = [el for el in listA if el in listB]

print(listC)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 2
# + Элемент неотрицательный
# + Элемент не кратен 3

import random

listA = [random.randint(-100,100) for _ in range(15)]

print(listA)

listB = [el for el in listA if not (el % 2)]
listC = [el for el in listA if not (el < 0)]
listD = [el for el in listA if (el % 3)]

print(listB)
print(listC)
print(listD)
