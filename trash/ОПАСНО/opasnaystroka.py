text = [['    Никита живет в Мытищах. Он живет там 5 лет. Мытищи '],
        ['-  это     город   в  Московской   области   России. В '],
        ['Мытищи   можно    доехать,    как    на    электричке, '],
        ['так   и    на  автобусе. Здесь   много    водохранилищ '],
        ['и     парков.   Мытищи        очень   хороший    город.']]

for i in range(len(text)):
    for j in range(len(text[i])):
        print(text[i][j],end='')
    print()
print()

# Переменные
p=0
counts=0
maxs=0
numberp=0
countt=0
deteck=False
lenstroki=0

for i in range(len(text)):
    for j in range(len(text[i][0])):
        if text[i][0][j]!='.':
            counts+=1
        else:
            p+=1
            if counts>maxs:
                maxs=counts
                numberp=p
            counts=0

print(' Кол-во символов:',maxs)
print(' Номер предложения:',numberp)
print(' Предложение с максимальным количеством символов: ')

for i in range(len(text)):
    for j in range(len(text[i][0])):
        if deteck:
            lenstroki+=1
            print(text[i][0][j],end='')
            if lenstroki>53:
                print()
                lenstroki=0
        if text[i][0][j]=='.':
            if countt==numberp-2:
                deteck=True
            else:
                deteck=False
            countt+=1


