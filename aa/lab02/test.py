from main import *


def comp_matr(matr1, matr2):
    if len(matr1) != len(matr2):
        return False
    if len(matr1) == 0 or len(matr1[0]) != len(matr2[0]):
        return False
    for i in range(len(matr1)):
        for j in range(len(matr1[i])):
            if matr1[i][j] != matr2[i][j]:
                return False
    return True


def comp(a, b, c, func1, func2):
    size = [a, b, c]
    matr1 = random_matr(size[0], size[1])
    matr2 = random_matr(size[1], size[2])
    res = np.zeros((size[0], size[2]))
    return comp_matr(func1(size[0], size[1], size[2], matr1, matr2, res),
                    func2(size[0], size[1], size[2], matr1, matr2, res))


def test():
    err = 0
    if not comp(3, 3, 3, classic, vinograd):
        err += 1
    if not comp(3, 3, 3, classic, vinograd_opt):
        err += 1
    if not comp(3, 3, 3, vinograd, vinograd_opt):
        err += 1

    if not comp(3, 4, 5, classic, vinograd):
        err += 1
    if not comp(3, 4, 5, classic, vinograd_opt):
        err += 1
    if not comp(3, 4, 5, vinograd, vinograd_opt):
        err += 1

    if not comp(5, 5, 5, classic, vinograd):
        err += 1
    if not comp(5, 5, 5, classic, vinograd_opt):
        err += 1
    if not comp(5, 5, 5, vinograd, vinograd_opt):
        err += 1

    if err:
        print('Зафиксированно ', err, 'ошибок !!!')
    else:
        print('Все тесты пройдены успешно')


if __name__ == '__main__':
    test()
