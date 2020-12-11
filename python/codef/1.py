t = int(input(''))
b = []

for i in range(t):
    n, m = map(int, input().split())

    if (n == 1):
        summa = 0
    elif (n == 2):
        summa = m
    else:
        cell = n // 2

        elem_int = m // cell

        mod_m = m % cell

        summa = 0

        if (n % 2 == 0):
            cell -= 1

            elem_int = m // cell

            mod_m = m % cell
            
        summa += elem_int * 2 * cell
            
        summa += mod_m * 2

    b.append(summa)
    
for i in range(t):
    print(b[i])
