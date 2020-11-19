def F(x):
    k = x ^ 2 - 1
    return k


def F1(x):
    k = 2*x
    return k


def F2(x):
    k = 2
    return k


# 1. Метод Ньютона
# Строятся касательные к графику функции в точке приближения (x0)
def Neuton(a, b):
    x0 = (a + b) / 2
    xn = F(x0)
    xn1 = xn - F(xn) / F1(xn)
    while abs(xn1 - xn) > eps:
        xn = xn1
        xn1 = xn - F(xn) / F1(xn)
    return xn1


# 2. Упрощенный метод Ньютона
# Если производная непрерывна, то ее значение близи простого корня практически
# постоянно. Поэтому можем вычислить производную одиин раз в точке x0
def New_Neuton(a, b, eps):
    x0 = (a + b) / 2
    xn = F(x0)
    xn1 = xn - F(xn) / F1(x0)
    while abs(xn1 - xn) > eps:
        xn = xn1
        xn1 = xn - F(xn) / F1(x0)
    return xn1


# 3. Метод секущих.
# Строятся не касательрные, а секущие
def sekush(a, b, eps):
    x1 = (a + b) / 2
    x2 = x1 + 2 * eps
    x1n = F(x1)
    xn = F(x2)
    xn1 = xn - (x1n - xn) / (F(x1n) - F(xn)) * F(xn)
    while abs(xn1 - xn) > eps:
        x1n = xn
        xn = xn1
        xn1 = xn - (x1n - xn) / (F(x1n) - F(xn)) * F(xn)
    return xn1


# 4. Метод хорд
# Отличие от метода секущих: в методе секущих берутся последние рассчитанные
# точки, а в методе хорд - точки, в которых функция имеет разный знак
def hord(a, b, eps):
    c = 0
    x = 0
    if F(a) * F2(a) > 0:
        c = a
    elif F(b) ** F2(b) > 0:
        c = b
    if F(a) * F2(a) < 0:
        x = a
    elif F(b) * F2(b) < 0:
        x = b
    dx = F(x) * (x - c) / (F(x) - F(c))
    x -= dx
    while abs(dx) > eps:
        dx = F(x) * (x - c) / (F(x) - F(c))
        x -= dx
    return x


# 5. Метод половинного деления
# Происходит сужение интервала, в котором находится нужный корень
def polovina(a, b, eps):
    while abs(b + a) > eps:
        c = (b - a) / 2
        if F(c) == 0:
            break
        elif F(a) * F(c) < 0:
            b = c
        else:
            a = c
    return c


# 6. Комбинированный метод
# Выбор нового отрезка от точки пересения хорды с осью х до точки пересечения
# касательной с осью х, на которой функция меняет знак и содержит ответ
def kombi(a, b, eps):
    x = 0
    while abs(a - b) > 2 * eps:
        if F(a) * F2(a) < 0:
            a = a - F(a) * (a - b) / (F(a) - F(b))
        elif F(a) * F2(a) > 0:
            a = a - F(a) / F1(a)
        if F(b) * F2(b) < 0:
            b = b - F(b) * (b - a) / (F(b) - F(a))
        elif F(b) * F2(b) > 0:
            b = b - F(b) / F1(b)
        x = (a + b) / 2
    return x


# 7. Метод Стеффенсона
def steff(a, b, eps):
    x0 = (a + b) / 2
    xn = x0 - F(x0) ** 2 / (F(x0 + f(x0)) - F(x0))
    while abs(xn - x0) > eps:
        x0 = xn
        xn = x0 - F(x0) ** 2 / (F(x0 + f(x0)) - F(x0))
    return xn


# 8. Метод итераций
def iter(a, b, eps):
    x0 = (a + b) / 2
    x1 = F(x0)
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = F(x0)
    return x1