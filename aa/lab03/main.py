import numpy as np
import random

from time import process_time


def menu():
    print('\n🚀 Меню: ')
    print('1) Сортировка рандомного массива заданного размера (пузырьком)')
    print('2) Сортировка рандомного массива заданного размера (выбором)')
    print('3) Сортировка рандомного массива заданного размера (расческой)')
    print('4) Сравнение по времени')


def time_analyze(function, iterations=100, size=5):
    t1 = process_time()
    for _ in range(iterations):
        start(size, function, False)
    t2 = process_time()
    return (t2 - t1) / iterations


def start(size, func, printable):
    arr = prepare_arr(size)
    if printable:
        print(arr)

    arr = func(arr, size)
    if printable:
        print(arr)
    return arr


def prepare_arr(size):
    arr = []
    for i in range(size):
        arr.append(i)
    random.shuffle(arr)
    return arr


def empty(arr, n):
    return arr

def analyze_time(iteration=10, size=10):
    print("Размер матриц: ", size)
    time_empty = time_analyze(empty, iteration, size)
    print("   Время на создание и заполнение массива : ", "{0:.8f}".format(time_empty))
    time_bubble = time_analyze(bubble, iteration, size) - time_empty
    print("   Сортировка пузырьком                   : ", "{0:.8f}".format(time_bubble))
    time_selection = time_analyze(selection, iteration, size) - time_empty
    print("   Сортировка выбором                     : ", "{0:.8f}".format(time_selection))
    time_comb = time_analyze(comb, iteration, size) - time_empty
    print("   Сортировка расческой                   : ", "{0:.8f}".format(time_comb))

    print('P.S. все результаты получены с учетом времени на создание и иницаилизации массивов')


# ======================================================================================================================
def bubble(arr, n):
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            j += 1
        i += 1
    return arr


def selection(arr, n):
    i = 0
    while i < n - 1:
        j = i + 1
        mina = arr[i]
        mini = i
        while j < n:
            if arr[j] < mina:
                mina = arr[j]
                mini = j
            j += 1
        tmp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = tmp
        i += 1
    return arr


def comb(arr, n):
    gap = (n * 10 // 13)

    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = False
        i = 0
        m = n - gap
        while i < m:
            if arr[i + gap] < arr[i]:
                tmp = arr[i]
                arr[i] = arr[i + gap]
                arr[i + gap] = tmp
                swapped = True
            i += 1
        gap = (gap * 10 // 13) or swapped
    return arr


if __name__ == '__main__':
    while True:
        menu()
        case = input('Выберите пункт меню: ')

        if case == '1':
            size = int(input('  Введите размер массива: '))
            start(size, bubble, True)
        elif case == '2':
            size = int(input('  Введите размер массива: '))
            start(size, selection, True)
        elif case == '3':
            size = int(input('  Введите размер массива: '))
            start(size, comb, True)
        elif case == '4':
            size = int(input('  Введите размер массива: '))
            iteration = int(input('  Введите количество итераций: '))
            analyze_time(iteration, size)

