t = int(input(''))
a = []

for i in range(t):
    x, y, n = map(int, input().split())

    tmp = n // x * x + y
    if (tmp > n):
        tmp -= xA
    
    a.append(tmp)

for i in range(t):
    print(a[i])
