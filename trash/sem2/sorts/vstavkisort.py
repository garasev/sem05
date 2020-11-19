from time import *
from random import *
li=[uniform(-10**9,10**9) for i in range(10000)]
for i in range(len(li)):
    key=li[i]
    start_time = time()
    j=i-1
    while li[j]>key and j>=0:
        li[j+1]=li[j]
        j-=1
    print(li)
    li[j+1]=key
    print("%s seconds" % (time() - start_time))
print(li)
