t = int(input(''))
a = []
arr = []

for i in range(t):
    n, k = map(int, input().split())
    arr = []
    arr = input().split()[:n]
    #print(arr)

    x = 0
    ans = 0
    count = 0

    for i in range(n):
        arr[i] = (- int(arr[i])) % k
        if (arr[i] != 0):
            count += 1

    
    while count != 0:
        print(arr)
        #print(count)
        i = 0
        flag = 0
        while i < n and flag == 0:
            if (arr[i] == x and x != 0):
                arr[i] -= x
                flag = 1
                count -= 1
            i += 1
            
        i = 0
        while i < n and flag == 0:
            if (arr[i] > x and x != 0):
                arr[i] -= x
                flag = 1
            i += 1
            
        x += 1
        if (x == k):
            x = 0
        ans += 1
    print(arr)
    a.append(ans)

for i in range(t):
    print(a[i])
