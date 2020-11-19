li=[5,2,7,4,0,9,8,6]
for i in range(len(li)):
    j=i-1
    key=li[i]
    while li[j]>key and j>=0:
        li[j+1]=li[j]
        j-=1
    li[j+1]=key
print(li)
ne smog bez help