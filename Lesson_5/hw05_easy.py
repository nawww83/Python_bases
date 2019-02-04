# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def make_dir(name):
    try:
        os.mkdir(name)
        print('Директория создана')
    except FileExistsError:
        print('Директория уже существует')

def remove_dir(name):
    try:
        os.rmdir(name)
        print('Директория удалена')
    except FileNotFoundError:
        print('Нет такой директории')

def change_dir(name):
    os.chdir(name)
    print('Директория изменена на ' + os.getcwd())


def main():
    for i in range(1,10):
        path = os.path.join(os.getcwd(), 'dir_' + str(i))
        make_dir(path)

    for i in range(1,10):
        path = os.path.join(os.getcwd(), 'dir_' + str(i))
        remove_dir(path)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

    listA = os.listdir('.')
    print('Папки текущей директории:')
    [print(el) for el in listA if os.path.isdir(el)]

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS

    dn,fn = os.path.split(__file__)
    dest = 'copy'

    try:
        os.mkdir(dest)
    except FileExistsError:
        pass

    data = open(fn).read()
    open(os.path.join(dest, fn), 'w').write(data)


if __name__ == '__main__':
    main()

