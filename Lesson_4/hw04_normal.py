# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re
import random

strA = ''.join([chr(random.randint(65,122)) for _ in range(20)])

print(strA)

# a)
pattern = '[a-z]+'
listA = re.findall(pattern, strA)

print(listA)

# b)
listB = list(strA)
listC = []
strB = ''
for l in listB:
    if l.islower():
        strB = strB + l
    elif strB:
        listC.append(strB)
        strB = ''

print(listC)

# Задание-2:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import os

path = os.path.join('.','mn.txt')
with open(path,'w') as f:
    [f.write(str(random.randint(0,9))) for _ in range(2500)]

mn = []
with open(path) as f:
    mn = f.readline()

ln = []
for i in range(0,9):
    pattern_n = '[' + str(i) + ']+'
    mn_n = re.findall(pattern_n, mn)
    max_l = 0
    for el in mn_n:
        max_l = len(el) if (len(el) > max_l) else max_l
    lnf = list(filter(lambda x: len(x) == max_l, mn_n))
    if lnf:
        ln.append(lnf[0])

lnt = []
max_l = 0
for el in ln:
    max_l = len(el) if (len(el) > max_l) else max_l
lnf = list(filter(lambda x: len(x) == max_l, ln))
if lnf:
    lnt.append(lnf)

print(lnt)
