li=[5,2,7,4,0,9,8,6]
for i in range(1,len(li)):
    l,r=-1,i
    key=li[i]
    while l<r-1:
        mid=(r+l)//2
        if key<li[mid]:
            r=mid
        else:
            l=mid
    for j in range(i,r,-1):
        li[j]=li[j-1]
    li[r]=key
print(li)