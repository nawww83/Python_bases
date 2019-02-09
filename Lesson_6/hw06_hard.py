'''
Задание-1: Решите задачу:

Дана ведомость расчета заработной платы (файл "data/workers").
Рассчитайте зарплату всех работников, зная что они получат полный оклад,
если отработают норму часов. Если же они отработали меньше нормы,
то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
удвоенную ЗП, пропорциональную норме.
Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

С использованием классов.
Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
каждый работник получал строку из файла

'''

import os

class Worker:
    def __init__(self, info_str):
        self.info_list = info_str.split()

    @property
    def name(self):
        return self.info_list[0]

    @property
    def surname(self):
        return self.info_list[1]    

    @property
    def oklad(self):
        return float(self.info_list[2])

    @property
    def position(self):
        return self.info_list[3]

    @property
    def rate(self):
        return float(self.info_list[4])

    def zp(self, hours):
        rate = self.rate
        less = float(hours <= rate)
        up = float(int(hours - rate))
        oklad = self.oklad
        return round(less * hours/rate * oklad + (1 - less) * (up/rate + 1) * oklad, 2)


pathW = os.path.join('data', 'workers')
pathH = os.path.join('data', 'hours_of')

def make_key(line):
    lw = line.split()
    return lw[0] + lw[1]

ws = {} # Список рабочих в виде словаря

with open(pathW, 'r') as f:
    lh = []
    for line in f:
        line = line.strip() # защита от пробельных строк
        if line:
            if not lh: # Header
                lh = line.split()
            else:
                key = make_key(line)
                ws[key] = Worker(line)

with open(pathH, 'r') as f:
    lh = []
    for line in f:
        line = line.strip() # защита от пробельных строк
        if line:
            if not lh: # Header
                lh = line.split()
            else:
                key = make_key(line)
                hours = float(line.split()[2])
                zp = ws[key].zp(hours)
                print(ws[key].name + ' ' + ws[key].surname + ' получит з/п ' + str(zp) + ' рупий')



