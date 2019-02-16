'''
Задание_1. Создать класс. В конструктор передать два параметра - два числа.
Создать второй класс. В конструкторе первого предусмотреть создание
объекта второго класса. Кроме того, в первом классе предусмотреть три метода,
в которых делегировать получение остатка от деления, результата деления и целой
части от деления в методы второго класса (предусмотреть вычисление в соотв. методах
второго класса).
'''

class A:
    def __init__(self, v1, v2):
        self.B = B(v1, v2)

    def res(self):
        return self.B.res()

    def div(self):
        return self.B.div()

    def idiv(self):
        return self.B.idiv()


class B:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def res(self):
        return self.v1 % self.v2

    def div(self):
        return self.v1 / self.v2

    def idiv(self):
        return self.v1 // self.v2

a1 = A(23,4)

a2 = A(25,5)

print(a1.res(), a1.div(), a1.idiv())
print(a2.res(), a2.div(), a2.idiv())

