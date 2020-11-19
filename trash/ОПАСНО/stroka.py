print(' Введите строку: ')
s=str(input())
a=[]
k=0
for i in range(len(s)):
    if s[i]!=' ':
        k=k+1
    else:
        if k!=0:
            a.append(k)
        k=0
if k!=0:
    a.append(k)
sr=0
ss=0
for i in range(len(a)):
    ss=ss+a[i]

if len(a)!=0:
    sr=ss/len(a)
else:
    print(' Нет слов! ')
count=0
k=0
for i in range(len(s)):
    if s[i]!=' ':
        k=k+1
    else:
        if k>sr:
            count=count+1
        k=0
print(' Массив длин слов:',a)
print(' Ср. ар. длин слов:',sr)
if k>sr:
    count=count+1
if count!=0:
    print(' Кол-во слов длина которых больше ср. ар. всех длин:',count)
