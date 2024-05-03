import numpy as np
import pandas as pd

# Define the transition matrix
# P_excel = pd.read_excel("Gora3.xlsx", index_col=0)
# P = P_excel.values

P = np.array([
    [0.000, 0.437, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.364, 0.000, 0.000, 0.000, 0.010, 0.189, 0.000, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.000, 0.262, 0.489, 0.000, 0.000, 0.000, 0.000, 0.249, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.139, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.221, 0.000, 0.000, 0.000, 0.323, 0.317, 0.000, 0.000],
    [0.416, 0.000, 0.295, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.288],
    [0.000, 0.000, 0.000, 0.888, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.112, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.299, 0.000, 0.000, 0.251, 0.000, 0.400, 0.049, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.316, 0.000, 0.000, 0.217, 0.000, 0.385, 0.082, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000, 0.410, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.590, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.000, 0.394, 0.337, 0.000, 0.000, 0.000, 0.000, 0.270, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000, 0.653, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.347, 0.000],
    [0.000, 0.000, 0.000, 0.130, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.870, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.319, 0.000, 0.000, 0.260, 0.000, 0.280, 0.141, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.000, 0.345, 0.349, 0.000, 0.000, 0.000, 0.000, 0.306, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.000, 0.746, 0.120, 0.000, 0.000, 0.000, 0.000, 0.135, 0.000, 0.000, 0.000, 0.000],
    [0.158, 0.000, 0.164, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.678],
    [0.000, 0.075, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.479, 0.000, 0.000, 0.000, 0.198, 0.248, 0.000, 0.000]
])

# Define the number of states
n = P.shape[0]


#TODO Проанализировать эргодическую цепь Маркова; найти период цепи d; выделить множества циклических состояний, на которые распадается цепь;


def findSetsOfCyclicStates(P):
    m = np.zeros(0,)
    for i in range(n):
        mj = np.zeros(0)
        for j in range(n):
            if P[i, j] != 0:
                mj = np.append(mj,  j+1)
        q = True
        if mj not in m:
        for arr in m:
            if arr
        if q:
             m = np.append(m, mj)
    return m

m = findSetsOfCyclicStates(P)
print(m.shape)
# Define the number of iterations
t = 8000

# Initialize the matrix W
W = np.zeros((n, n))

# Calculate the matrix W using the Cesaro sum
for i in range(t):
    W += np.linalg.matrix_power(P, i)
W /= t

# Print the matrix W
print(W)


# Calculate the indicator of row uniformity
def indicator(W):
    rows = [W[i, :] for i in range(n)]
    max_dist = 0
    for i in range(n):
        for j in range(i + 1, n):
            dist = np.linalg.norm(rows[i] - rows[j])
            if dist > max_dist:
                max_dist = dist
    return max_dist


print("Indicator of row uniformity:", indicator(W))

t_values = [50, 100, 200, 400, 800, 1000, 10000]
indicator_values = []
for t in t_values:
    W = np.zeros((n, n))
    for i in range(t):
        W += np.linalg.matrix_power(P, i)
    W /= t
    indicator_values.append(indicator(W))

import matplotlib.pyplot as plt

plt.plot(t_values, indicator_values)
plt.xlabel('t')
plt.ylabel('Indicator of row uniformity')
plt.show()
