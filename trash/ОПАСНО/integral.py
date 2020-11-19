# Переменные
# a,b-начальное и конечное значения функции
# n1,n2 -

from math import*
# Функция вычисления значения подынтегрального выражения
def f(a):
    b=a*a
    return(b)

a=float(input(' Введите нижнюю границу интегрирования: '))
b=float(input(' Введите верхнюю границу интегрирования: '))
#while not(a>0 and b>0 and a!=b):
   # print(' ОШИБКА!!!')
   # print(' Введите другие грацы интегрирования: 0<a<b ')
   # a=float(input(' Введите нижнюю границу интегрирования: '))
   # b=float(input(' Введите верхнюю границу интегрирования: '))
n1,n2 =map(int,input(' Введите n1 и n2 через пробел: ').split())
m1,m2 = n1,n2

# Метод левых прямоугольников
h1=abs((b-a))/n1
h2=abs((b-a))/n2
z1=0
z2=0
if a>b:
    a,b=b,a
x=a
for i in range(n1):   
    z1=z1+h1*abs(f(x))
    x=x+h1
x=a
for i in range(n2):   
    z2=z2+h2*abs(f(x))
    x=x+h2

# Метод параболы
zp1=f(a)+f(b)
zp2=f(a)+f(b)
x=a+h1
i1=4
i2=2
for i in range(1,n1):
    zp1=zp1+i1*abs(f(x))
    x=x+h1
    i1,i2=i2,i1
x=a+h2
i1=4
i2=2
for i in range(1,n2):
    zp2=zp2+i1*abs(f(x))
    x=x+h2
    i1,i2=i2,i1
zp2=zp2*h2/3
zp1=zp1*h1/3

# Вывод
print('┌──────────────────────┬─────────────────────┬────────────────────────┐\
')
print('│          n           │{:21.6}│{:24.6}│'.format(float(n1),float(n2)))
print('├──────────────────────┼─────────────────────┼────────────────────────┤\
')
print('│ метод левых прямо-ов │{:21.9}│{:24.8}│'.format((z1),(z2)))
print('├──────────────────────┼─────────────────────┼────────────────────────┤\
')
print('│    метод парабол     │{:21.9}│{:24.8}│'.format((zp1),(zp2)))
print('└──────────────────────┴─────────────────────┴────────────────────────┘\
')

# Точное значение интеграла
#it=(log(b)*log(b)*log(b)-log(a)*log(a)*log(a))/3
it=(b*b*b-a*a*a)/3
print(' Точное значение интеграла: ','{:.8}'.format(it))

print(' Метод парабол более точный.') 
print(' Рассмотрим метод левых прямоугольников.')
print()
eps=float(input(' Введите точность eps: '))
n1=2
n2=4
h1=abs((b-a))/n1
h2=abs((b-a))/n2
in1=0
in2=0
x=a
for i in range(n1):   
    in1=in1+h1*abs(f(x))
    x=x+h1
x=a
for i in range(n2):   
    in2=in2+in2*abs(f(x))
    x=x+h2
        
while abs(in2-in1)>eps:
    n1=n2
    n2=n2*2
    h1=abs((b-a))/n1
    h2=abs((b-a))/n2
    in1=0
    in2=0
    x=a
    for i in range(n1):   
        in1=in1+h1*abs(f(x))
        x=x+h1
    x=a
    for i in range(n2):   
        in2=in2+h2*abs(f(x))
        x=x+h2
print(' Для вычисления интеграла с заданной точностью потребовалось:',n2,\
      'разбиваний.')
print()
print(' Найдем абсолютную и относительную ошибку:')
print(' Метод левых прямоугльников. Разбиений:',m1)
oa=abs(it-z1)
if it!=0:
    oo=abs((it-z1)/it)
print(' Абсолютная ошибка:','{:2.7e}'.format(oa))
print(' Относительная ошибка:','{:2.7e}'.format(oo))
print()
print(' Метод левых прямоугльников. Разбиений:',m2)
oa=abs(it-z2)
if it!=0:
    oo=abs((it-z2)/it)
print(' Абсолютная ошибка:','{:2.7e}'.format(oa))
print(' Относительная ошибка:','{:2.7e}'.format(oo))
