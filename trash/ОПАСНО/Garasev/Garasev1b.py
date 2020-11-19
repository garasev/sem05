# Garasev. Вариант №6
from math import*

print(' Введите элементы массива В(10) через пробел: ')
b=list(map(float,input().split()))
num=[0]
maxe=b[0]
num[0]=1
for i in range(1,len(b)):
    if b[i]==maxe:
        num.append(i+1)
    if b[i]>maxe:
        num.clear()
        num.append(i+1)
        maxe=b[i]
print('Исходный массив В',end='      ')
for i in range(len(b)):
    print(b[i],end=' ')
print()
# вывод массива num
print('Полученный массив NUM',end='  ')
for i in range(len(num)):
    print(num[i],end=' ')
print()
# сжатие
for i in range(len(num)):
    b.remove(maxe)
if len(b)!=0:
    print('Сжатый массив В',end='        ')
    for i in range(len(b)):
        print(b[i],end=' ')
else:
    print('Все элементы одинаковые.')    
