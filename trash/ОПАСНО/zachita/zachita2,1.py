# │─├┼ 
from math import*
x1=float(input(' Введите начальное значение функции: '))
x2=float(input(' Введите конечное значение функции: '))
h=float(input(' Введите шаг функции: '))
i=x1
minw=2*sin(x1)
maxw=2*sin(x1)
while i<=x2:
    w=2*sin(i)
    if w>maxw:
        maxw=w
    if w<minw:
        minw=w    
    i+=h    
m=(maxw-minw)/50
po=trunc(abs(minw)/m)
eps=m
z1=minw+(maxw-minw)/3
z2=minw+(maxw-minw)/3*2
print('{:11.1f}'.format(minw),end='')
print('{:17.1f}'.format(z1),end='')
print('{:17.1f}'.format(z2),end='')
print('{:17.1f}'.format(maxw))     
print('         ├────────────────┼────────────────┼────────────────┼─>')
if minw<=0 and maxw>=0:
    while x1<=x2:
        w=2*sin(x1)
        px=trunc(abs(minw-w)/m)
        if abs(w)<=eps:
            print('{:8.2f}'.format(x1),' ',' '*po,'x',sep='')
        elif w<0:
            print('{:8.2f}'.format(x1),' ',' '*px,'x',' '*(po-px-1),'│',sep='')
        else:
            print('{:8.2f}'.format(x1),' ',' '*po,'│',' '*(px-po-1),'x',sep='')
        x1+=h    
if minw>0:
    while x1<=x2:
        w=2*sin(x1)
        px=trunc(abs(minw-w)/m)
        print('{:8.2f}'.format(x1),' ',' '*px,'x',sep='')
        x1+=h
if maxw<0:
    while x1<=x2:
        w=2*sin(x1)
        px=trunc(abs(minw-w)/m)
        print('{:8.2f}'.format(x1),' ',' '*px,'x',sep='')
        x1+=h         

