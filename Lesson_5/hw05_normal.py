# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
# ИСПОЛЬЗОВАТЬ МОДУЛЬ OS и SHUTIL

import sys
import os
import hw05_easy as my_os

def list_dir(name=''):
    print(os.listdir())

do = {
'1': my_os.change_dir,
'2': list_dir,
'3': my_os.remove_dir,
'4': my_os.make_dir
}

while True:
    print('1 - Перейти в директорию')
    print('2 - Просмотреть содержимое текущей директории')
    print('3 - Удалить директорию')
    print('4 - Создать директорию')
    print('q - Завершить работу')
    f = input()
    name = ''
    if f.isdigit() and not f == '2':
        name = input('Введите имя директории:')
    if do.get(f):
        do[f](name)
    elif f == 'q':
        sys.exit()

