import numpy as np
import random

from time import process_time

def menu():
    print('\n🚀 Меню: ')
    print('1) Перемножение рандомных матриц заданного размера (Классическое)')
    print('2) Перемножение рандомных матриц заданного размера (Виноград)')
    print('3) Перемножение рандомных матриц заданного размера (оптимизированный Виноград)')
    print('4) Сравнение по времени')


def time_analyze(function, iterations=100, length=5):
    size = []
    for _ in range(3):
        size.append(length)

    t1 = process_time()
    for _ in range(iterations):
        start(size, function, False)
    t2 = process_time()

    return (t2 - t1) / iterations


def input_size():
    print('┌─────────────────┐')
    print('│ Матрица A [N,M] │')
    print('│ Матрица B [M,K] │')
    print('└─────────────────┘')
    size = [int(input('  введите N:')), int(input('  введите M:')), int(input('  введите K:'))]
    return size


def create_matr(len1, len2):
    matr = np.zeros((len1, len2))
    return matr


def random_matr(len1, len2):
    matr = create_matr(len1, len2)
    for i in range(len1):
        for j in range(len2):
            matr[i][j] = random.randint(0, 9)
    return matr


def print_matr(matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            print(int(matr[i][j]), end=' ')
        print('')


# ======================================================================
def start(size, function, printable=False):
    matr1 = random_matr(size[0], size[1])
    if printable:
        print('Матрица A:')
        print_matr(matr1)

    matr2 = random_matr(size[1], size[2])
    if printable:
        print('Матрица B:')
        print_matr(matr2)

    res = np.zeros((size[0], size[2]))
    res = function(size[0], size[1], size[2], matr1, matr2, res)

    if printable:
        print('Результирующая матрица:')
        print_matr(res)
    return res


def empty(n, m, k, matr1, matr2, res):
    pass


def classic(n, m, k, matr1, matr2, res):
    i = 0
    while i < n:
        j = 0
        while j < k:
            l = 0
            while l < m:
                res[i][j] += matr1[i][l] * matr2[l][j]
                l += 1
            j += 1
        i += 1
    return res


def vinograd(n, m, k, matr1, matr2, res):
    mulH = [0] * n
    mulV = [0] * k

    i = 0
    while i < n:
        j = 0
        while j < m // 2:
            mulH[i] = mulH[i] + matr1[i][j * 2] * matr1[i][j * 2 + 1]
            j += 1
        i += 1

    i = 0
    while i < k:
        j = 0
        while j < m // 2:
            mulV[i] = mulV[i] + matr2[j * 2][i] * matr2[j * 2 + 1][i]
            j += 1
        i += 1

    i = 0
    while i < n:
        j = 0
        while j < k:
            res[i][j] = -mulH[i] - mulV[j]
            l = 0
            while l < m // 2:
                res[i][j] = res[i][j] + (matr1[i][2 * l + 1] + matr2[2 * l][j]) * \
                            (matr1[i][2 * l] + matr2[2 * l + 1][j])
                l += 1
            j += 1
        i += 1

    if m % 2 == 1:
        i = 0
        while i < n:
            j = 0
            while j < k:
                res[i][j] = res[i][j] + matr1[i][m - 1] * matr2[m - 1][j]
                j += 1
            i += 1
    return res


def vinograd_opt(n, m, k, matr1, matr2, res):
    mulH = [0] * n
    mulV = [0] * k

    tmp = m - m % 2

    i = 0
    while i < n:
        j = 0
        while j < tmp:
            mulH[i] += matr1[i][j] * matr1[i][j + 1]
            j += 2
        i += 1

    i = 0
    while i < k:
        j = 0
        while j < tmp:
            mulV[i] += matr2[j][i] * matr2[j + 1][i]
            j += 2
        i += 1

    i = 0
    while i < n:
        j = 0
        while j < k:
            buff = -mulH[i] - mulV[j]
            l = 0
            while l < tmp:
                buff += (matr1[i][l + 1] + matr2[l][j]) * (matr1[i][l] + matr2[l + 1][j])
                l += 2
            res[i][j] = buff
            j += 1
        i += 1

    if m % 2 == 1:
        i = 0
        tmp = m - 1
        while i < n:
            j = 0
            while j < k:
                res[i][j] += matr1[i][tmp] * matr2[tmp][j]
                j += 1
            i += 1
    return res


def analyze_time(iteration=10, size=10):
    print("Размер матриц: ", size)
    time_empty = time_analyze(empty, iteration, size)
    print("   Время на создание и заполнение матриц   : ", "{0:.8f}".format(time_empty))
    time_classic = time_analyze(classic, iteration, size) - time_empty
    print("   Классическое умножение                  : ", "{0:.8f}".format(time_classic))
    time_vinograd = time_analyze(vinograd, iteration, size) - time_empty
    print("   Умножение по Винограду                  : ", "{0:.8f}".format(time_vinograd))
    time_vinograd_opt = time_analyze(vinograd_opt, iteration, size) - time_empty
    print("   Умножение по оптимизированному Винограду: ", "{0:.8f}".format(time_vinograd_opt))
    print('P.S. все результаты получены с учетом времени на создание и иницаилизации матриц')


if __name__ == '__main__':
    while True:
        menu()
        case = input('Выберите пункт меню: ')

        if case == '1':
            start(input_size(), classic, True)
        elif case == '2':
            start(input_size(), vinograd, True)
        elif case == '3':
            start(input_size(), vinograd_opt, True)
        elif case == '4':
            iteration = int(input('  *введите итерации: '))
            size = int(input('  *введите размер: '))
            analyze_time(iteration, size)
