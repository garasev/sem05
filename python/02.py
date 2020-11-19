count = int(input())
result = []


def minus_counter(n, m, matr):
    counter = 0
    for i in range(n):
        for j in range(m):
            matr[i][j] = int(matr[i][j])
            if matr[i][j] < 0:
                counter += 1
    return counter


def find_min(n, m, matr):
    min_item = abs(matr[0][0])
    for i in range(n):
        for j in range(m):
            if abs(matr[i][j]) < min_item:
                min_item = abs(matr[i][j])
    return min_item


def sum_matr(n, m, matr):
    s = 0
    for i in range(n):
        for j in range(m):
            s += abs(matr[i][j])
    return s


for _ in range(count):
    n, m = map(int, input().split())
    matr = []
    for i in range(n):  # A для цикла для записей строк
        tmp = input()
        tmp = tmp.split(' ')
        matr.append(tmp)

    minus = minus_counter(n, m, matr)
    s = sum_matr(n, m, matr)
    if minus % 2 == 1:
        s -= 2 * find_min(n, m, matr)

    result.append(s)

for i in range(count):
    print(result[i])