# Garasev. Вариант №3
from math import*

k=int(input(' Введите K(k<=12): '))
z=[[0]*k for i in range(k)]
print(z)
for i in range(k):
    for j in range(k):
        if i>k-j:
            z[i][j]=0    
for i in range(k):
    for j in range(k):
        print(a[i][j],end=' ')
    print()
