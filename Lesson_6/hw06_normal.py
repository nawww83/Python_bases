'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''

from math import sqrt

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        # Примем за начало отсчета точку p1
        self.w = {'x': p2['x'] - p1['x'], 'y': p2['y'] - p1['y']}
        self.v = {'x': p3['x'] - p1['x'], 'y': p3['y'] - p1['y']}

    def square(self):
        wv = (self.w['x']*self.v['x'] + self.w['y']*self.v['y']) # Скалярное произведение векторов
        ww = sqrt(self.w['x']**2 + self.w['y']**2) # Норма вектора
        vv = sqrt(self.v['x']**2 + self.v['y']**2)
        cosA = wv / ww / vv # Косинус угла между векторами
        return 0.5 * ww * vv * sqrt(1 - cosA**2) # S =  a * b / 2 * sinA
    
    def height(self): # Одна из высот
        ww = sqrt(self.w['x']**2 + self.w['y']**2)
        vv = sqrt(self.v['x']**2 + self.v['y']**2)
        wwvv = sqrt((self.w['x'] - self.v['x'])**2 + (self.w['y'] - self.v['y'])**2)
        sq = self.square()
        return [2 * sq / ww, 2 * sq / vv, 2 * sq / wwvv] # Если верить wiki

    def path(self):
        ww = sqrt(self.w['x']**2 + self.w['y']**2)
        vv = sqrt(self.v['x']**2 + self.v['y']**2)
        wwvv = sqrt((self.w['x'] - self.v['x'])**2 + (self.w['y'] - self.v['y'])**2)
        return ww + vv + wwvv
        

t1 = Triangle({'x': 0, 'y': 0}, {'x': 0, 'y': 2}, {'x': 2, 'y': 0})
print('Плошадь треугольника: ' + str(t1.square()))
print('Высоты треугольника: ' + str(t1.height()))
print('Периметр треугольника: ' + str(t1.path()))

