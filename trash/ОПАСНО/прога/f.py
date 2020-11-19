from math import*
# Контрольные точки:
# При a=1.2
# q1=a**3-23.8*a*a+44.9*a-10.34 = 10.996
# q2=a*log(a)-6=-5.78121413185
# q3=sqrt(abs(q1*q2))=7,97309416687
# При a=3
# q1=a**3-23.8*a*a+44.9*a-10.34 = −62,84
# q2=a*log(a)-6=-2.704163134
# q3=sqrt(abs(q1*q2))=13,0357052491
# При a=6
# q1=a**3-23.8*a*a+44.9*a-10.34 = −381,74
# q2=a*log(a)-6=4,75055681537
# q3=sqrt(abs(q1*q2))=42,5849452119

a1=float(input(' Введите начальное значение функции: '))
a2=float(input(' Введите конечное значение функции: '))
a3=float(input(' Введите шаг функции: '))
print(' ┌──────┬───────────────┬───────────────┬───────────────┬───────\
────────┐ ')
print(' │номер │ ''   аргумент ',' │  ''     q1    ',' │ '\
      '     q2    ','  │ ''     q3    ','  │ ')
print(' ├──────┴───────────────┴───────────────┴───────────────┴───────\
────────┤ ')
p=trunc((a2-a1)/a3+1)
i=0
a=a1
max1=a**3-23.8*a*a+44.9*a-10.34
max2=a*log(a)-6
min2=a*log(a)-6
for k in range(1,p+1):
    i+=1    
    q1=a**3-23.8*a*a+44.9*a-10.34
    q2=a*log(a)-6
    q3=sqrt(abs(q1*q2))
    if q2<min2:
        min2=q2
    if q1>max1:
        max1=q1
    if q2>max2:
        max2=q2
    if q1<1000:
        print(' │ ',i,'\t  {:1.4f}'.format(a),' ','\t  {:10.4f}'.format(q1)\
          ,' ','\t  {:10.4f}'.format(q2),' ','\t  {:10.4f}'.format(q3),'\t│')
    else:
        print(' │ ',i,'\t  {:1.4f}'.format(a),' ','\t  {:10.4e}'.format(q1)\
          ,' ','\t  {:10.4e}'.format(q2),' ','\t  {:10.4e}'.format(q3),'\t│')
    a=a1+k*a3 
print(' └──────────────────────────────────────────────────────────────\
────────┘ ')
         
r=round(max1-max2,4)
if r>100000:
    print(' Разность между максимальными значениями\
функций q1 и q2: ','{:10.4e}'.format(r))
else:
    print(' Разность между максимальными значениями функций q1 и q2: ',r)










z1=min2+(max2-min2)/4
z2=min2+(max2-min2)/2
z3=min2+3*(max2-min2)/4
if min2>=1000:
    print('{:16.1e}'.format(min2),'{:12.1e}'.format(z1),'{:12.1e}'.format(z2),\
    '{:12.1e}'.format(z3),'{:10.1e}'.format(max2))
elif min2<1000 and z1>=1000:
    print('{:16.1f}'.format(min2),'{:12.1e}'.format(z1),'{:12.1e}'.format(z2),\
    '{:12.1e}'.format(z3),'{:10.1e}'.format(max2))
elif z1<1000 and z2>=1000:
    print('{:16.1f}'.format(min2),'{:12.1f}'.format(z1),'{:12.1e}'.format(z2),\
    '{:12.1e}'.format(z3),'{:10.1e}'.format(max2))
elif z2<1000 and z3>=1000:
    print('{:16.1f}'.format(min2),'{:12.1f}'.format(z1),'{:12.1f}'.format(z2),\
    '{:12.1e}'.format(z3),'{:10.1e}'.format(max2))
elif z3<1000 and max2>=1000:
    print('{:16.1f}'.format(min2),'{:12.1f}'.format(z1),'{:12.1f}'.format(z2),\
    '{:12.1f}'.format(z3),'{:10.1e}'.format(max2))
else:
    print('{:16.1f}'.format(min2),'{:12.1f}'.format(z1),'{:12.1f}'.format(z2),\
    '{:12.1f}'.format(z3),'{:10.1f}'.format(max2))    
print('           ├────────────┼────────────┼────────────┼──────────┼─>')
a=a1
i=1
m=round((max2-min2)/50,4)
p0=trunc(abs(min2)/m)
eps=m*0.66
if min2<=0 and max2>=0:
    while a<=a2:
        q2=a*log(a)-6    
        px=trunc(abs(q2-min2)/m)
        
        if abs(q2)<eps:
            if i%2!=0:
                print('{:10.4f}'.format(a),' ',' '*px,'X',sep='')
            else:
                print('           ',' '*px,'X',sep='')
        elif q2<0:
            if i%2!=0:
                print('{:10.4f}'.format(a),' ',' '*px,'X',' '*(p0-px-1),'│\
',sep='')
            else:
                print('           ',' '*px,'X',' '*(p0-px-1),'│',sep='')
        else:
            if i%2!=0:
                print('{:10.4f}'.format(a),' ',' '*p0,'│',' '*(px-p0-1),'X\
',sep='')
            else:
                print('           ',' '*p0,'│',' '*(px-p0-1),'X\
',sep='')
        a+=a3
        i+=1
    print('{:9}'.format('Y'),' '*(p0),'▼') 
if min2>0:
    while a<=a2:
        q2=a*log(a)-6    
        px=trunc(abs(q2-min2)/m)
        
        if i%2!=0:
            print('{:10.4f}'.format(a),' ',' '*px,'X',sep='')
        else:
            print('           ',' ',' '*px,'X',sep='')        
        a+=a3
        i+=1  
if max2<0:
    while a<=a2:
        q2=a*log(a)-6    
        px=trunc(abs(q2-min2)/m)
        
        if i%2!=0:
            print('{:10.4f}'.format(a),' ',' '*px,'X',sep='')
        else:
            print('           ',' '*px,'X',sep='')        
        a+=a3
        i+=1
















