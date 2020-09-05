
import numpy as np
import string
import random

from time import time

symbols = string.ascii_letters + string.digits
debug = False


# Вспомогательные функции
def min_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= c and b <= a:
        return b
    elif c <= a and c <= b:
        return c


def random_string(length):
    return ''.join(random.choice(symbols) for i in range(length))


def time_analyze(function, iteration, length=5):
    t1 = time()
    for i in range(iteration):
        s1 = random_string(length)
        s2 = random_string(length)
        function(s1, s2)
    t2 = time()
    return (t2 - t1) / iter


def input_s1_s2():
    s1 = input('  Input first word: ')
    s2 = input('  Input second word: ')
    return s1, s2


def start_func(func):
    s1, s2 = input_s1_s2()
    func(s1, s2, True)


def operations(s1, s2, matr):
    def pathfinder(m, i, j):
        if i > 0 and j > 0 and m[i - 1][j - 1] < m[i][j]:
            pathfinder(m, i - 1, j - 1)
            print('R', end=' ')
        elif i > 0 and m[i - 1][j] < m[i][j]:
            pathfinder(m, i - 1, j)
            print('D', end=' ')
        elif j > 0 and m[i][j - 1] < m[i][j]:
            pathfinder(m, i, j - 1)
            print('I', end=' ')
        elif i > 0 and j > 0 and m[i - 1][j - 1] == m[i][j]:
            pathfinder(m, i - 1, j - 1)
            print('M', end=' ')

    pathfinder(matr, len(s1), len(s2))


def output_matrix(s1, s2, matr):
    print("\n   ", end=" ")
    for i in s2:
        print(i, end=" ")

    for i in range(len(matr)):
        if i:
            print("\n" + s1[i - 1], end=" ")
        else:
            print("\n ", end=" ")
        for j in range(len(matr[i])):
            print(int(matr[i][j]), end=" ")
    print("\n")


def int_inputer(str, value):
    tmp = input(str)
    if tmp.isnumeric():
        tmp = int(tmp)
    else:
        tmp = value
    return tmp


# Функции подсчета расстояния Левеншейна
# Levenshtein distance
def calc_dist_matrix(s1, s2, printable=False):
    matr = np.eye(len(s1) + 1, len(s2) + 1)
    for i in range(len(s1) + 1):
        matr[i][0] = i
    for j in range(len(s2) + 1):
        matr[0][j] = j
    for i in range(len(s1)):
        for j in range(len(s2)):
            d1 = matr[i + 1][j] + 1
            d2 = matr[i][j + 1] + 1
            if s1[i] == s2[j]:
                d3 = matr[i][j]
            else:
                d3 = matr[i][j] + 1
            matr[i + 1][j + 1] = min(d1, d2, d3)

    if printable:
        print('Matrix: \n', matr)
        output_matrix(s1, s2, matr)
        print('Operation: \n   ', end='')
        operations(s1, s2, matr)


def calc_dist_recur(s1, s2, printable=False):
    if debug or printable:
        print(s1, s2)

    if s1 == '' or s2 == '':
        return abs(len(s1) - len(s2))

    tmp = 0 if (s1[-1] == s2[-1]) else 1
    return min(calc_dist_recur(s1[:-1], s2) + 1,
               calc_dist_recur(s1, s2[:-1]) + 1,
               calc_dist_recur(s1[:-1], s2[:-1]) + tmp)


def calc_dist_recur_matrix(s1, s2, printable=False):
    matr = np.full((len(s1) + 1, len(s2) + 1), -1)

    def calc_value(i, j):
        if matr[i][j] != -1:
            return matr[i][j]
        else:
            tmp = 0 if (s1[i - 1] == s2[j - 1]) else 1
            return min(calc_value(i - 1, j) + 1,
                       calc_value(i, j - 1) + 1,
                       calc_value(i - 1, j - 1) + tmp,)

    for i in range(len(s1) + 1):
        matr[i][0] = i
    for j in range(len(s2) + 1):
        matr[0][j] = j

    if printable:
        print('Return:', calc_value(len(s1), len(s2)))


def calc_dist_damerau(s1, s2, printable=False):
    matr = np.eye(len(s1) + 1, len(s2) + 1)
    for i in range(len(s1) + 1):
        matr[i][0] = i
    for j in range(len(s2) + 1):
        matr[0][j] = j
    for i in range(len(s1)):
        for j in range(len(s2)):
            d1 = matr[i + 1][j] + 1
            d2 = matr[i][j + 1] + 1
            if s1[i] == s2[j]:
                d3 = matr[i][j]
            else:
                d3 = matr[i][j] + 1
            if s1[i] == s2[j - 1] and s1[i - 1] == s2[j] and i > 0 and j > 0:
                d4 = matr[i - 1][j - 1] + 1
            else:
                d4 = d1
            matr[i + 1][j + 1] = min(d1, d2, d3, d4)

    if printable:
        print('Matrix: \n', matr)


if __name__ == '__main__':

    while True:
        case = input('\n\nMenu: \n \
1) Levenshtein distance matrix\n \
2) Levenshtein distance recursion\n \
3) Levenshtein distance matrix-recursion\n \
4) Damerau Levenshtein distance matrix\n \
5) Time analyze\n \
case: ')
        if case == '1':
            start_func(calc_dist_matrix)
        elif case == '2':
            start_func(calc_dist_recur)
        elif case == '3':
            start_func(calc_dist_recur_matrix)
        elif case == '4':
            start_func(calc_dist_damerau)
        elif case == '5':

            iter = int_inputer('Input number of iterations:', 100)
            i1 = int_inputer('Input lower limit:', 1)
            i2 = int_inputer('Input upper limit:', 10)

            for i in range(i1, i2 + 1):
                print("String length: ", i)
                print("   Levenshtein matrix           : ", "{0:.8f}".format(time_analyze(calc_dist_matrix,
                                                                                           iter, i)))
                print("   Levenshtein recursion        : ", "{0:.8f}".format(time_analyze(calc_dist_recur,
                                                                                           iter, i)))
                print("   Levenshtein matrix-recursion : ", "{0:.8f}".format(time_analyze(calc_dist_recur_matrix,
                                                                                           iter, i)))
                print("   Damerau Levenshtein matrix   : ", "{0:.8f}".format(time_analyze(calc_dist_damerau,
                                                                                           iter, i)))
