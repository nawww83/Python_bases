# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# !!!Смотри в easy


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

pathW = os.path.join('data', 'workers')
pathH = os.path.join('data', 'hours_of')

moneys = {}
titles = {}
norms = {}
hours = {}

with open(pathW, 'r') as f:
    lh = []
    for line in f:
        line = line.strip() # защита от пробельных строк
        if line:
            if not lh: # Header
                lh = line.split()
            else:
                lw = line.split()
                key = lw[0]+lw[1]
                moneys[key] = float(lw[2])
                titles[key] = lw[3]
                norms[key] = float(lw[4])

with open(pathH, 'r') as f:
    lh = []
    for line in f:
        line = line.strip() # защита от пробельных строк
        if line:
            if not lh: # Header
                lh = line.split()
            else:
                lw = line.split()
                key = lw[0]+lw[1]
                hours[key] = float(lw[2])

moneys_total = {}

for key, value in moneys.items():
    h = hours[key]
    hn = norms[key]
    less = float(h <= hn)
    up = float(int(h - hn))
    moneys_total[key] = round(less * h/hn * value + (1 - less) * (up/hn + 1) * value, 2)

for key in moneys_total:
    print(key, titles[key], ' получит ', moneys_total[key])


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))



path = os.path.join('data', 'fruits.txt')
lb = []
dictF = {}
with open(path, 'r') as f:
    for line in f:
        line = line.strip() # защита от пробельных строк
        if line: 
            b = line[0] # Первая буква
            if not (b in lb):
                lb.append(b)
                pp = os.path.join('data', 'fruits_' + b + '.txt')
                dictF[b] = open(pp, 'w')
            dictF[b].write(line + '\n')

for f in dictF:
    dictF[f].close()


