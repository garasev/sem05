from math import*

n=int(input('Введите кол-во точек: '))
x=[0]*n
y=[0]*n
p=0
for i in range(n):
    x[i],y[i]=map(float,input('Координаты точки: ').split())
    if p==0 and y[i]>=0:
        ny=sqrt(x[i]*x[i]+y[i]*y[i])
        nb=sqrt(x[i]*x[i]+y[i]*y[i])
        nyi=i
        nbi=i
        p=1
for i in range(n):
    k=sqrt(x[i]*x[i]+y[i]*y[i])
    if k>ny and y[i]>=0:
        ny=k
        nyi=i
    if k<nb and y[i]>=0:
        nb=k
        nbi=i
print('Координаты наиболее удаленной точки: ',x[nyi],y[nyi])
print('Координаты наиболее близкой точки: ',x[nbi],y[nbi])
p=sqrt((x[nyi]-x[nbi])**2+(y[nyi]-y[nbi])**2)
print('Расстояние между этими точками',round(p,4))
