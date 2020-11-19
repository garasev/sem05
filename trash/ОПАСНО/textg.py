text = [['    Никита живет в Мытищах. Он живет там 5 лет. Мытищи'],
        ['-  это     город   в  Московской   области   России. В'],
        ['Мытищи   можно    доехать,    как    на    электричке,'],
        ['так   и    на  автобусе. Здесь   много    водохранилищ'],
        ['и     парков.   Мытищи        очень   хороший    город.']]


strokar=''
vibor=-1
maxk=0
k=0
kp=0
sch=0
dlinastr=[0]*len(text)
while vibor!=0:
    vibor=int(input())
    for i in range(len(text)):
            k=0            
            for j in range(len(text[i][0])-1):
                if (text[i][0][j]!=' ')or(text[i][0][j]==' ' and
                                        text[i][0][j+1]!=' '):
                    k+=1
            if text[i][0][len(text[i][0])-1]!=' ':
                k+=1
            dlinastr[i]=k
            if maxk<k:
                maxk=k
    if vibor==1:
        for i in range(len(text)):
            if dlinastr[i]==maxk:
                for j in range(len(text[i][0])-1):
                    if (text[i][0][j]!=' ')or(text[i][0][j]==' ' and
                                          text[i][0][j+1]!=' '):
                        strokar=strokar+text[i][0][j]
                if text[i][0][len(text[i][0])-1]!=' ':
                    strokar=strokar+text[i][0][len(text[i][0])-1]
            else:
                kp=0
                sch=0
                for j in range(len(text[i][0])-1):
                    if text[i][0][j]==' ' and text[i][0][j+1]!=' ':
                        kp+=1
                n=(maxk-dlinastr[i])//kp
                dp=(maxk-dlinastr[i])%kp
                for j in range(len(text[i][0])-1):
                    if text[i][0][j]!=' ':
                        strokar=strokar+text[i][0][j]
                    if text[i][0][j]==' ' and text[i][0][j+1]!=' ':
                        if sch<dp:
                            sch+=1
                            strokar=strokar+' '*(n+2)
                        else:
                            strokar=strokar+' '*(n+1)
                if text[i][0][len(text[i][0])-1]!=' ':
                    strokar=strokar+text[i][0][len(text[i][0])-1]
            text[i][0]=strokar
            print(text[i][0])
            strokar=''
    if vibor==2:
        for i in range(len(text)):
            for j in range(len(text[i][0])-1):
                if (text[i][0][j]!=' ')or(text[i][0][j]==' ' and
                                        text[i][0][j+1]!=' '):
                    strokar=strokar+text[i][0][j]
            if text[i][0][len(text[i][0])-1]!=' ':
                strokar=strokar+text[i][0][len(text[i][0])-1]
            print(strokar)
            strokar=''
    if vibor==3:
        for i in range(len(text)):
            strokar=strokar+' '*(maxk-dlinastr[i])
            for j in range(len(text[i][0])-1):
                if (text[i][0][j]!=' ')or(text[i][0][j]==' ' and
                                        text[i][0][j+1]!=' '):
                    strokar=strokar+text[i][0][j]
            if text[i][0][len(text[i][0])-1]!=' ':
                strokar=strokar+text[i][0][len(text[i][0])-1]
            print(strokar)
            strokar=''
    if vibor==4:
        old=input(' Введите слово, которое заменяем:')
        new=input(' Введите слово, НА которое заменяем:')
        for i in range(len(text)):
            text[i][0]=text[i][0].replace(old,new)
            print(text[i][0])
        maxk=0
    if vibor==5:
        old=input(' Введите слово, которое хотите удалить:')
        new=''
        for i in range(len(text)):
            
            text[i][0]=text[i][0].replace(old,new)
            print(text[i][0])
        maxk=0
