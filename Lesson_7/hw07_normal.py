'''
Задача-1: Создать класс Матрица. В конструктор класса передавать переменную
содержащую матрицу в виде списка списков. В конструкторе класса преобразовать
список списков в привычный матричный вид. Переопределить стандартное поведение
методов __add__ и __str__ класса. Создать два экземпляра класса Матрица с данными.
Метод __add__ должен реализовывать сложение матриц, а __str__ - вывод итоговой
матрицы.
'''

class Matrix:
    def __init__(self, lm):
        self.lm = lm
        self.sm = ''
        for el in map(str, lm):
            self.sm += (el + '\n')

    def __add__(self, other):
        # Это, конечно, ребус был...
        return Matrix(\
            [\
                 ( [(i+j) for (i,j) in zip(x, y)] ) for (x,y) in zip(self.lm, other.lm) \
            ] \
                     )

    def __str__(self):
        return 'Матрица \n{}'.format(self.sm)

M1 = Matrix([[1,-2,5], [3,4,4]])
M2 = Matrix([[5,6,2], [3,5,9]])

M3 = M1 + M2

print(M3)
