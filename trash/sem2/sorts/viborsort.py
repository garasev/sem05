li=[5,2,7,4,0,9,8,6]
n=0
for i in range(1,len(li)):
    m=li[n]
    indmin=n+1
    for j in range(indmin-1,len(li)):
        if li[indmin]>li[j]:
            indmin=j
    li[n],li[indmin]=li[indmin],li[n]
    print(li)
    n+=1
print(li)