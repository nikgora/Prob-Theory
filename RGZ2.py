import pandas as pd

import numpy as np

P_excel = pd.read_excel("Gora2.xlsx", header=None)
P = P_excel.values


def is_regular(matrix, max_power=1000):
    power = 1
    new_matrix = np.copy(matrix)
    while power <= max_power:
        if np.all(new_matrix > 0):
            return True, power
        new_matrix = np.dot(new_matrix, matrix)
        power += 1
    return False, None


def stationary_distribution(matrix):
    _, n = matrix.shape
    q = matrix.T - np.eye(n)
    ones = np.ones(n)
    q[-1] = ones
    b = np.zeros(n)
    b[-1] = 1
    return np.linalg.lstsq(q, b, rcond=None)[0]


def mean_first_return(matrix):
    n = len(matrix)
    w = stationary_distribution(matrix)
    i = (np.eye(n))
    # Обчислення Z
    z = np.linalg.inv(i - (matrix - w))
    # Обчислення Z_dg
    z_dg = np.diagflat(z.diagonal())
    j = np.ones((n,n))
    k = i - z + np.dot(j, z_dg)
    D = np.zeros((n, n))
    # Обчислення зворотних значень елементів W
    inv_w = 1.0 / w
    # Заповнення діагональних елементів матриці D
    for i in range(n):
        D[i, i] = inv_w[i]
    # Обчислення матриці E
    e = np.dot(k, D)
    return e


is_regular_chain, k = is_regular(P)
if is_regular_chain:
    print("Ланцюг Маркова є регулярним із показником ступеня:", k)
    # Обчислення вектора стаціонарних станів
    w = stationary_distribution(P)
    print("Вектор стаціонарних станів w:")
    print(w)
    # Знаходження матриці середніх часів перших повернень
    E = mean_first_return(P)
    print("Матриця середніх часів перших повернень E:")
    print(E)
else:
    print("Ланцюг Маркова не є регулярним.")

