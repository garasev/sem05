t = int(input(''))
a = []


for i in range(t):
    n = int(input())
    s = str(input())
    string = []
    
    for i in range(n):
        if (s[i] == '('):
            string.append('(')
        if (s[i] == ')'):
            string.append(')')
            
    
    st = 0
    ans = 0
    i = 0
    
    while i < n:
        
        if (string[i] == '('):
            st += 1
            
        if (string[i] == ')'):
            if (st == 0):
                # perenos v konec
                for j in range(i, n - 1):
                    string[j] = string[j + 1] 
                string[n - 1] = ')'
                ans += 1
                i -= 1
            else:
                st -= 1
        i += 1
    a.append(ans)

for i in range(t):
    print(a[i])
