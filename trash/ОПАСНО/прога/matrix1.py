from math import*
print(' Заполните матрицу А(8,8) ')
n=int(input(' Введите кол-во строк и столбцов квадратной матрицы n<=8: '))
print('Введите n элементов через пробел в каждой строке')
b=[]
a=[]
a=[[int(j) for j in input().split()] for i in range(n)]
for i in range(n):
    for j in range(n):
        if j>i and a[i][j]<0:
            b.append(a[i][j])
print(' Матрица a: ')
for q in a:
    print(q)
if b==[]:
    print(' В матрице А нет отрицательных элементов над главной диагональю')
else:
    maxb=b[0]
    maxi=0
    mini=0
    minb=b[0]
    print(' Измененный массив В: ')
    for i in range(len(b)):
        if minb>b[i]:
            minb=b[i]
            mini=i
        if maxb<b[i]:
            maxb=b[i]
            maxi=i
    b[maxi],b[mini]=b[mini],b[maxi]
    print(b)

            
