li=[5,2,7,4,0,9,8,6]
n=1
k=0
while n<len(li):
    for i in range(len(li)-n):
        if li[i]>li[i+1]:
            li[i],li[i+1]=li[i+1],li[i]
    n+=1
    for j in range(len(li)-n,k,-1):
        if li[j]<li[j-1]:
            li[j],li[j-1]=li[j-1],li[j]
    k+=1
    print(li)
print(li)