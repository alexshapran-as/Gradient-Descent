import numpy as np
from prettytable import PrettyTable

th = ["Step", "x", "y", "f(x,y)"]
td = []

columns = len(th)
table = PrettyTable(th)

def f(vars):
    # Function: f(x,y)=15*х^2 + 30*y^2
    return 15 * vars[0] ** 2 + 30 * vars[1] ** 2


def gradient_descent(alpha=0.01, eps=0.001):
    vars_prev = np.array([100, 100])
    vars = np.array([50, 50])
    for _ in range(100000):
        table.add_row([_, np.round(vars[0], 3), np.round(vars[1], 3), np.round(f(vars), 5)])
        if np.sum((vars - vars_prev) ** 2) < eps ** 2:
            break
        vars_prev = vars
        vars = vars_prev - alpha * np.array(20 * vars_prev[0], 20 * vars_prev[1])
    return vars


vars_min = gradient_descent()
table.add_row(["", "min x", "min y", "f(min x, min y)"])
table.add_row(["", vars_min[0], vars_min[1], f(vars_min)])
print(table)
