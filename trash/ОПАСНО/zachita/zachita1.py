

from math import*

x1,y1=map(float,input('Введите координаты первой точки: ').split())
x2,y2=map(float,input('Введите координаты второй точки: ').split())
x3,y3=map(float,input('Введите координаты третей точки: ').split())
x4,y4=map(float,input('Введите координаты произвольной точки: ').split())

#r1,r2,r3 - расстояние от точки до сторон треугольника

r1=abs((y2-y1)*x4-(x2-x1)*y4+x2*y1-x1*y2)/sqrt((y2-y1)**2+(x2-x1)**2)
r2=abs((y3-y2)*x4-(x3-x2)*y4+x3*y2-x2*y3)/sqrt((y3-y2)**2+(x3-x2)**2)
r3=abs((y1-y3)*x4-(x1-x3)*y4+x1*y3-x3*y1)/sqrt((y1-y3)**2+(x1-x3)**2)
rmax=r1
if r2>rmax:
    rmax=r2
if r3>rmax:
    rmax=r3
rmax=round(rmax,6)    
print('Расстояние от точки до наиболее удаленной стороны: ',rmax)    
