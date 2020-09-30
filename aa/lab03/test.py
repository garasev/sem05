from main import *


def compare_arr(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

def sorted_arr(size, start=0):
    arr = []
    if start == 0:
        for i in range(size):
            arr.append(i)
    else:
        for i in range(size):
            arr.append(size - i - 1)
    return arr


def full_test(func):
    err = 0
    # Проверка алгоритма на массивах длиной от 1 до 100
    for i in range(1, 100):
        if not compare_arr(start(i, func, False), sorted_arr(i, 0)):
            err += 1

    # Проверка алгоритма на ста отсортированных массивах
    for i in range(1, 100):
        if not compare_arr(func(sorted_arr(i, 0), i), sorted_arr(i, 0)):
            err += 1

    # Проверка алгоритма на ста обратно-отсортированных массивах
    for i in range(1, 100):
        if not compare_arr(func(sorted_arr(i, 1), i), sorted_arr(i, 0)):
            err += 1

    if err:
        print('Зафиксированно ', err, 'ошибок для функции:', func.__name__)
    else:
        print('Все тесты пройдены успешно для функции:', func.__name__)

if __name__ == '__main__':
    full_test(bubble)
    full_test()
    full_test(bubble)
