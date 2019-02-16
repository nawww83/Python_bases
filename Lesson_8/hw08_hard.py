'''
Задание_1. Создайте свое исключение для проверки вводимого числа.
Исключение должно возбуждаться, если пользователь ввел отрицательное число.
Также предусмотрите тот, случай, что пользователь ввел не число, а строку
(здесь можно применить встроенное исключение).
'''

class NonPositiveInputException(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return 'NonPositiveInputException: введено отрицательное число. Ожидается положительное или ноль.'

class PositiveNum:
    def __init__(self, val):
        try:
            float(val)
            if val < 0:              
                raise NonPositiveInputException
            else:
                self.val = val
        except ValueError:
            print('Введено не число!')
        else:
            print('Все хорошо')
        finally:
            pass

try:
    p = PositiveNum(5)
except NonPositiveInputException as np:
    print(np)
finally:
    pass

try:
    p = PositiveNum(-3)
except NonPositiveInputException as np:
    print(np)
finally:
    pass

try:
    p = PositiveNum('a')
except NonPositiveInputException as np:
    print(np)
finally:
    pass

