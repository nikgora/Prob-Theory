import numpy as np
import pandas as pd

# Define the transition matrix
P_excel = pd.read_excel("Gora3.xlsx", index_col=0)
P = P_excel.values


# Define the number of states
n = P.shape[0]


#TODO Fix Reading from exel


def findSetsOfCyclicStates(P):
    m = []
    for i in range(n):
        mj = []
        for j in range(n):
            if P[i, j] != 0:
                mj.append((j+1))
        if mj not in m:
            m.append(mj)

    return m

m = findSetsOfCyclicStates(P)
print("Number of cycle sets:", len(m))
print("Cycle sets")
for mj in m:
    print(mj)
# Define the number of iterations
t = 800

# Initialize the matrix W
W = np.zeros((n, n))

# Calculate the matrix W using the Cesaro sum
for i in range(t):
    W += np.linalg.matrix_power(P, i)
W /= t

# Print the matrix W
print("Matrix W stationary calculus: ")
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
