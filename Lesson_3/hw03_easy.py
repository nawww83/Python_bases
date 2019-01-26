# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def subro(l, d=1, off=-1):
    """
    Вспомогательная функция для цепочечного суммирования
    """
    if l[off].isdigit():
        nd = int(l[off])+d
        if -off >= len(l)+1:
            return l
        if nd < 10:
            l[off] = str(nd)
            return l                
        else:
            l[off] = list(str(nd))[-1]                    
            l = subro(l, nd//10, off-1)
    else:
        l = subro(l, d, off-1)
    return l

def my_round(v, n):
    vs = str(v)
    ls = list(vs)
    if ls.count('.') > 0:
        pp = ls.index('.')
    else:
        pp = -1
    if pp < 0 or pp == len(ls) - 1:
        return v
    nr = pp+n+1
    npad = nr - len(ls)
    if npad > 0: # дополнение нулями
        for i in range(0,npad):
            ls.append('0')
    lr = ls[0:nr]
    sr = ''.join(lr)
    if len(lr) == len(ls): # если нет отбрасываемых разрядов
        return float(sr)
    else:
        d = int(ls[nr])
        if d > 4: # "правило" математики
            lr = subro(lr)
        return float(''.join(lr))


v = 0.9367
print(my_round(v, 3))

v = 0.9367
print(my_round(v, 1))

v = 0.9367
print(my_round(v, 7))

v = 0.9
print(my_round(v, 1))

v = 0.9
print(my_round(v, 0))

v = 0.99
print(my_round(v, 1))

v = 46.
print(my_round(v, 1))

   
# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def is_lucky(n):
    ND = 6
    ns = str(n) # число в строку
    if len(ns) < ND:
        return False
    nll = list(ns[:ND//2]) # первую половину цифр в список
    nlr = list(ns[ND//2:])
    sl = sum(list(map(lambda x : int(x), nll))) # перевод элементов списка в int
    sr = sum(list(map(lambda x : int(x), nlr)))
    return sl == sr

# 1+2+3 <> 4+5+6
no1 = 123456
print(is_lucky(no1))

# 1+2+3 = 0+1+5
no2 = 123015
print(is_lucky(no2))

