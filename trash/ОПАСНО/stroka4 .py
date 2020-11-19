# Procedure
# c - кол-во удаленных строк
# a - массив
# k - кол-во строк
def ydalenei_sort(a,k):
    al=['a','b','c','d','e','f','g','h','i','j','k',
        'l','m','n','o','p','q','r','s','t','u','v',
        'w','x','y','z']
    c=0
    i=0
    while (k-c)>i:
        if a[i][0] not in al:
            a.remove(a[i])
            c+=1
            i-=1
        i+=1   
    for i in range(k-c):
        for j in range(i+1,k-c):
            if a[i][0]>a[j][0]:
                a[i],a[j]=a[j],a[i]

# VVod
# k - кол-во строк
# x - массив
k=int(input(' Введите кол-во строк: '))
print(' Введите матрицу по строчно через пробел: ')
x=[]
for i in range(k):
    x.append([(j) for j in input().split()])
print(' Исходная матрица: ')
for q in x:
    print(q)
ydalenei_sort(x,k)
print(' Измененная матрица: ')
for q in x:
    print(q)
