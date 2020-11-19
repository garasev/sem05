from math import*
c1=float(input(' Введите начальное значение функции: '))
c2=float(input(' Введите конечное значение функции: '))
h=float(input(' Введите шаг функции: '))
i=c1
mins=c1*c1*c1+c1-1
maxs=c1*c1*c1+c1-1
while i<=c2:
    s=i*i*i+i-1
    if s>maxs:
        maxs=s
    if s<mins:
        mins=s    
    i+=h
m=(maxs-mins)/50
po=trunc(abs(mins)/m)
eps=m
z1=mins+(maxs-mins)/3
z2=mins+(maxs-mins)/3*2
if abs(mins)<1000:
    print('{:12.2f}'.format(mins),end='')
else:
    print('{:16.2e}'.format(mins),end='')
if abs(z1)<1000:
    print('{:17.2f}'.format(z1),end='')
else:
    print('{:17.2e}'.format(z1),end='')
if abs(z2)<1000:
    print('{:17.2f}'.format(z2),end='')
else:
    print('{:17.2e}'.format(z2),end='')
if abs(maxs)<1000:
    print('{:17.2f}'.format(maxs))
else:
    print('{:17.2e}'.format(maxs))            
    
print('         ├────────────────┼────────────────┼────────────────┼─>')
if mins<=0 and maxs>=0:
    while c1<=c2:
        s=c1*c1*c1+c1-1
        px=trunc(abs(mins-s)/m)
        if abs(s)<=eps:
            print('{:8.2f}'.format(c1),' ',' '*po,'x',sep='')
        elif s<0:
            print('{:8.2f}'.format(c1),' ',' '*px,'x',' '*(po-px-1),'│',sep='')
        else:
            print('{:8.2f}'.format(c1),' ',' '*po,'│',' '*(px-po-1),'x',sep='')
        c1+=h    
if mins>0:
    while c1<=c2:
        s=c1*c1*c1+c1-1
        px=trunc(abs(mins-s)/m)
        print('{:8.2f}'.format(c1),' ',' '*px,'x',sep='')
        c1+=h
if maxs<0:
    while c1<=c2:
        s=c1*c1*c1+c1-1
        px=trunc(abs(mins-s)/m)
        print('{:8.2f}'.format(c1),' ',' '*px,'x',sep='')
        c1+=h         
