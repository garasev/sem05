from math import*
k=int(input('Введите К(3<=K<=38): '))
if k<=38 and k>=3:
    print('Вводите числа по 1 в строке: ')
    a=int(input())
    b=int(input())
    p=False
    n=0
    eks=0
    for i in range(2,k):
        c=int(input())    
        if a<b and b>c and p==False:
            p=True
            eks=b
            n=i
        if a>b and b<c and p==False:
            p=True
            eks=b
            n=i
        a=b
        b=c
    
    if n==0:
        print('Экстремума нет')
    else:
        print('Первый экстремум последовательности',eks,',его номер',n)
else:
    print('Введите другое К(3<=K<=38)')
