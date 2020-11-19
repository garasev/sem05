from math import*
p=list(map(float,input('Введите массив Р(10) в 1 строчку: ').split()))
c=0
r=1
if len(p)>10 or len(p)<=0:
    print('Введите массив в котором максимум 10 элементов')
else:
    for i in range(len(p)):
        if p[i]>0:
            c+=1
            r=r*p[i]
    if c!=0:
        rez=pow(r,1/c)
        print('Среднее геометрическое положительных элементов массива Р:',end=' ')
        if rez>=1000:
            print('{:1.2e}'.format(rez))
        else:
            print('{:1.4f}'.format(rez))
    else:
        print('В массиве Р нет положительных элементов')
