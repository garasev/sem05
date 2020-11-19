a=list(map(int,input(' Введите массив А через пробел: ').split()))
b=list(map(int,input(' Введите массив В через пробел: ').split()))
o=[]
r=[]
p=[]
k=0
c=0
for i in range(len(a)):
    o.append(a[i])
    r.append(a[i])
for i in range(len(b)):
    o.append(b[i])
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            r.pop(i-k)
            p.append(a[i])
            o.pop(i-c)
            c+=1
            k+=1

print(' Массив объединения: ',o)   
print(' Массив пересечения: ',p)
print(' Массив разности: ',r)
