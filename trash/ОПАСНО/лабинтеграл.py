from math import sqrt,log
def methodpr(a,b,n):
    h=(b-a)/n
    sum=0
    for i in range(1,n+1):
        x=a+i*h
        f=1/x/sqrt(x*x+1)
        sum+=f
    sum*=h
    return(sum)
def method38(a,b,n):
    h=(b-a)/n
    sum=0
    for i in range(n+1):
        x=a+i*h
        f=1/x/sqrt(x*x+1)
        if i==0 or i==n:
            sum+=f
        if i%3==0 and i!=0 and i!=n:
            f*=2
            sum+=f
        if i%3!=0 and i!=0 and i!=n:
            f*=3
            sum+=f
    sum*=3/8*h
    return (sum)
def tabl(n):
    print('┌','─'*27,'┬','─'*20,'┬','─'*20,'┐',sep='')
    print('│',' '*3,'Метод',' '*19,'│',' '*5,'n1 ={:4.0f}'.format(n1),' '*7,\
      '│',' '*5,'n2 ={:4.0f}'.format(n2),' '*7,'│',sep='')
    print('├','─'*27,'┼','─'*20,'┼','─'*20,'┤',sep='')
    print('│',' '*3,'Правые прямоугольники',' '*3,'│',' '*5,'{:0.7f}'.format\
      (methodpr(a,b,n1)),' '*n,'│',' '*5,'{:0.7f}'.format(methodpr(a,b,n2)),\
      ' '*n,'│',sep='')
    print('├','─'*27,'┼','─'*20,'┼','─'*20,'┤',sep='')
    print('│',' '*3,'Три восьмых',' '*13,'│',' '*5,'{:0.7f}'.format\
      (method38(a,b,n1)),' '*n,'│',' '*5,'{:0.7f}'.format(method38(a,b,n2))\
      ,' '*n,'│',sep='')
    print('└','─'*27,'┴','─'*20,'┴','─'*20,'┘',sep='')
def pervoobraz(x):
    F=log(x/(1+sqrt(x*x+1)))
    return(F)
def text1(a,b,n):
    print('Абсолютное значение при n=',n,':', '{:2.7f}'.format\
          (abs(Itochn-methodpr(a,b,n))))
    print('Относительное значение при n=',n,':','{:2.7f}'.format\
          (abs((Itochn-methodpr(a,b,n))/Itochn)))
def text2(a,b,n):
    print('Абсолютное значение при n=',n,':', '{:2.7f}'.format\
          (abs(Itochn-method38(a,b,n))))
    print('Относительное значение при n=',n,':','{:2.7f}'.format\
          (abs((Itochn-method38(a,b,n))/Itochn)))
def toch(a,b,n,e):
    n1=n
    while (abs(methodpr(a,b,2*n)-methodpr(a,b,n))>e):
        sum=methodpr(a,b,2*n)
        n*=2
    print('Вычислили интеграл при n=',n1,' до',n,'разбиений:','{:2.7f}'.format(sum))      
a=float(input('введите нижний предел интегрирования >0: '))
b=float(input('введите верхний предел интегрирования >0: '))
n1,n2= map(int,input('введите кол-во участков разбиения n1 и n2 отрезка[a,b]:\
').split())
if a<b:
    tabl(6)
else:
    tabl(5)
Itochn=pervoobraz(b)-pervoobraz(a)
print()
print('Точное значение интеграла: {:2.7f}'.format(Itochn))
print()
print('Для метода правые прямоугольники: ')
text1(a,b,n1)
text1(a,b,n2)
print()
print('Для метода три восьмых: ')
text2(a,b,n1)
text2(a,b,n2)
print()
print('Метод три восьмых более точный')
print('Вычислим с точность e интеграл для метода правые прямоугольники')
e=float(input('Введите точность e: '))
toch(a,b,n1,e)
toch(a,b,n2,e)
    

