from math import*
def boola(a,b,n):
    def f(x):
        y=x*x
        return(y)
    h=(b-a)/n
    x=a
    summa=7*f(x)
    x+=h
    for i in range(1,n):
        if i%4==1 or i%4==3:
            summa+=32*f(x)
        elif i%4==2:
            summa+=12*f(x)
        elif i%4==0:
            summa+=14*f(x)
        x+=h
    summa+=7*f(x)
    summa=summa*2*h/45
    print(summa)
    return(summa)
a=float(input(' Введите нижнюю границу интегрирования: '))
b=float(input(' Введите верхнюю границу интегрирования: '))
while not(b>a and a!=b):
    print(' ОШИБКА!!!')
    print(' Введите другие грацы интегрирования: a<b ')
    a=float(input(' Введите нижнюю границу интегрирования: '))
    b=float(input(' Введите верхнюю границу интегрирования: '))
eps=float(input(' Введите точность eps: '))
n1=2
n2=4
while abs(boola(a,b,n2)-boola(a,b,n1))>eps:
    n1,n2=n2,n2*2
print(' Для вычисления интеграла с заданной точностью потребовалось:',n2,\
      'разбиваний.')

        
        
