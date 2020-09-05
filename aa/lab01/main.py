
import numpy as np

# Функции подсчета расстояния Левеншейна
# Levenshtein distance

def min_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= c and b <= a:
        return b
    elif c <= a and c <= b:
        return c


def calc_dist_matrix(s1, s2):
    matrix = np.eye(len(s1) + 1, len(s2) + 1)
    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for j in range(len(s2) + 1):
        matrix[0][j] = j
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                pass
    print(matrix)


if __name__ == '__main__':
    calc_dist_matrix('print', 'prototype')
