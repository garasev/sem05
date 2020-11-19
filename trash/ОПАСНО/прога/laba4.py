from math import*
a=list(map(int,input('Введите эллементы массива A(10)через пробел:').split()))
b=list(map(int,input('Введите эллементы массива B(15)через пробел:').split()))
k=int(input('Введите число К: '))
for i in range(len(b)):
    a.insert(k+i,b[i])
print(a)
