t = int(input(''))
a = []

for i in range(t):
    n = int(input())
    tmp = n
    k2 = 0
    k3 = 0
    
    ans = 0
    while tmp != 1:
        f = 0
        if (tmp % 2 == 0):
            k2 += 1
            tmp /= 2
            f = 1
        if (tmp % 3 == 0):
            k3 += 1
            tmp /= 3
            f = 1
        if (f == 0):
            ans = -1
            break
    if (k2 > k3):
        ans = -1
    elif ans == 0:
        ans = k3 - k2 + k3
    a.append(ans)

for i in range(t):
    print(a[i])
