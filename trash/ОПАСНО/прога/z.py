from math import*

a,b=map(float,input('Коэффициенты a,b:').split())
x,y=map(float,input('Числа x,y:').split())


if x>0 :
    if a!=0:
        z=log(a*x)-12.34
    else:
        print('a=0')
else:
    z=tan(y)+ pow(a*b,0.5)
print('{0:.4f}'.format(z)) 
