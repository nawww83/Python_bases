# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y
# например, equation = 'y = -12x + 11111140.2121'

x = 4

eq = 'y = - 12x + 48.0'

eq = eq.replace(' ','')

pos_equal = eq.index('=')
pos_x = eq.index('x')

k = float(eq[pos_equal+1:pos_x])
bt = eq[pos_x+1:]

b = float(bt)
y = k * x + b

print(k,b,y)
