li=[5,2,7,4,0,9,8,6]
n=0
while n<len(li):
    for i in range(len(li)-n-1):
        if li[i]>li[i+1]:
            li[i],li[i+1]=li[i+1],li[i]
    n+=1
print(li)