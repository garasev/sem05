# Garasev. Вариант №6
from math import*

print(' Введите элементы массива В(10) через пробел: ')
b=list(map(float,input().split()))
num=[0]*len(b)
maxe=b[0]
num[0]=1
# 1 просмотр массива В для формирования массива NUM
for i in range(1,len(b)):
    if b[i]==maxe:
        num[i]=i+1
    if b[i]>maxe:
        num=[0]*len(b)
        num[i]=i+1
        maxe=b[i]
print('Исходный массив В',end='      ')
for i in range(len(b)):
    print(b[i],end=' ')
print()
# вывод массива num
print('Полученный массив NUM',end='  ')
for i in range(len(b)):
    if num[i]!=0:
        print(num[i],end=' ')
print()
# сжатие
k=0
for i in range(len(b)):
    if num[i]!=0:
        k=k+1
for i in range(k):
    for j in range(len(b)):
        if b[j]==maxe:
            for l in range(j,len(b)-1):
                b[l]=b[l+1]
# проверка
if num[len(b)-1]!=len(b):
    print('Сжатый массив В',end='        ')
    for i in range(len(b)-k):
        print(b[i],end=' ')
else:
    print('Все элементы одинаковые.')
        
        

        
