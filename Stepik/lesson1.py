a = 0
b = 0
c = 0
s = 0
p = 0
pi = 3.14
r = 0
tip_figure = (input())
if tip_figure == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a+b+c)/2
    s = (p*((p-a)*(p-b)*(p-c)))**0.5
    print(str(s))
elif tip_figure == 'прямоугольник':
    a = float(input())
    b = float(input())
    s = a*b
    print(str(s))
elif tip_figure == 'круг':
    r = float(input())
    s = pi*r**2
    print(str(s))
else:
    print('Нет такой фигуры')