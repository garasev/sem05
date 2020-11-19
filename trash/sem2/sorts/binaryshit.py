li=[5,2,7,4,0,9,8,6]
for i in range(1,len(li)):
    key=li[i]
    l=-1
    r=i
    while l<r-1:
        mid=(l+r)//2
        if key<li[mid]:
            r=mid
        else:
            l=mid
    for j in range(i,r,-1):
        li[j]=li[j-1]
    print(li)
    li[r]=key
print(li)