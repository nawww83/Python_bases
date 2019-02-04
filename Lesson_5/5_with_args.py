# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
import random

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <name> - создание копии файла name")
    print("rm <name> - удаление файла name")
    print("cd <name> - изменить директорию на name")
    print("ls - полный путь до текущей директории")


def test_dir(name):
    return bool(name)

def make_dir():
    test_dir(dir_name)
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy():
    if not test_dir(dir_name):
        print("Необходимо указать путь к файлу вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    dest_path = dir_path + str(num)
    shutil.copy(dir_path, dest_path)
    print('Файл ' + dir_path + ' скопирован в ' + dest_path)

def remove():
    if not test_dir(dir_name):
        print("Необходимо указать путь к файлу вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    if not os.path.isfile(dir_path):
        print(dir_path + ' не является файлом')
    elif input('Действительно удалить? 1 - да / 0 - нет:') == '1':
        os.remove(dir_path)
        print('Файл ' + dir_path + ' удален')  

def chdir():
    if not test_dir(dir_name):
        print("Необходимо указать путь вторым параметром")
        return
    try:
        os.chdir(dir_name)
        print('Директория изменена на ' + os.getcwd())
    except FileNotFoundError:
        print('Нет такой директории')

def ls():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy,
    "rm": remove,
    "cd": chdir,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

num = random.randint(1,65536)

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
