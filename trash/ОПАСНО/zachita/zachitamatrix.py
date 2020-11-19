from math import*

n=int(input('Введите кол-во строк матрицы W(10,15): '))
print('Введите элементы строк через пробел: ')
w=[[int(j) for j in input().split()] for i  in range(n)]

maxe=w[0][0]
m=len(w[0])
for i in range(n):
    for j in range(m):
        if w[i][j]>maxe:
            js=j
            maxe=w[i][j]
print('Максимальный элемент:',maxe)
print('Номер его слобца:',js)
for i in range(n):
    for j in range(js,m-1):
        w[i][j]=w[i][j+1]
    w[i][m-1]=0
for i in range(n):
    for j in range(m-1):
        print('{:3}'.format(w[i][j]),end=' ')
    print()
for i in range(n):
    s=0
    c=0
    for j in range(m-1):
        s=s+w[i][j]
    for j in range(m-1): 
        if w[i][j]>s:
            c=c+1
    print('В строчке №',i,' кол-во элементов:',c)
    print('Сумма:',s)
