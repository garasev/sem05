#binarysort
import time
import random
from random import *
start_time = time.time()
a=[]
for i in range(1000):
        a.append(randint(0,10000))
n=len(a)
for i in range(1,n):
    elem=a[i]
    l=-1
    r=i
    while l<r-1:
        t=(l+r)//2
        if elem<a[t]:
            r=t
        else:
            l=t
    for j in range(i,r+1,-1):
        a[j]=a[j-1]
    a[r]=elem
print(a)
print("--- %s seconds ---" % (time.time() - start_time))
