from math import*

x,y=map(float,input('Введите координаты точки: ').split())

if (y>x-1)or(x<0)or(y>0)or(x*x+y*y>2):
    print('Не принадлежит')
else:
    print('Принадлежит')
    
    
