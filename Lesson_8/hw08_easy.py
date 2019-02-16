'''
Задание 1. Реализовать класс-строитель. В его конструктор передать два списка.
Класс должен возвратить python-объект словарь. Проверить, что объект
создается корректно - создать экземпляр класса и обратиться к значению
элемента словаря, как к атрибуту класса.
'''

class Builder:
    def __init__(self, l1, l2):
        self.d = {}
        for k,v in  zip(l1, l2):
            self.d[k] = v
            setattr(self, k, v)
    
b = Builder(['name','surname'],['Ivan','Ivanov'])
print(b.name)
print(b.surname)

'''
Задание 2.
Создать класс-обертку для списка. Список передвайте в конструктор класса.
Реализуйте удаление всех элементов из списка через функцию clear.
Но функция должна применяться не к списку, а к экземпляру класса.
Внутри класса должно быть предусмотрено делегирование этой функции методу (clear)
списка.
'''

class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, attr):
        return getattr(self.wrapped, attr)

    def get(self):
        return self.wrapped

wl = Wrapper([1,2,3])
print(wl.get())

wl.clear()
print(wl.get())
