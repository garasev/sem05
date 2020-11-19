from math import*
from random import*
k=trunc(random()*36+3)
a=trunc(random()*11)
b=trunc(random()*11)
p=False
n=0
eks=0
print(k,a,b,end=' ')
for i in range(2,k):
    c=trunc(random()*11)
    print(c,end=' ')
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
print()
if n==0:
    print('Экстремума нет')
else:
    print('Первый экстремум последовательности',eks,',его номер',n)
