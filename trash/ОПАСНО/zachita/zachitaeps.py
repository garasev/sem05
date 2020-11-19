from math import*
eps=float(input('Введите точность: '))
t1=1
t2=-1/3
s=t1+t2
n=3
while eps<abs(t2-t1):
    t1=t2
    t2=pow(-1,n-1)/(2*n-1)
    s=s+t2
    n=n+1

s=4*s    
print('Cумма бесконечного ряда с точностью eps = {:0.6f}'.format(s))
