data=[2,6,1,6,9,34,346,87,42,6,2,8,3,2]
inc = len(data) // 2
while inc:
    for i, el in enumerate(data):
        print(i,el)
        while i >= inc and data[i - inc] > el:
            data[i] = data[i - inc]
            i -= inc
        data[i] = el
        print(data)
    if inc == 2:
        inc=1
    else:
        inc=int(inc * 5.0 / 11)
print(data)