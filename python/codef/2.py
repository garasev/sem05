t = int(input(''))
c = []

for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    count = 0

    while (True):
        if (min(a) >= max(b) or count == k):
            break
        
        a[count], b[n - count - 1] = b[n - count - 1], a[count]
        count += 1
        
    c.append(sum(a))

for i in range(t):
    print(c[i])
