import numpy as np
# entering given datas
x = np.array([0, 1, 2, 3, 4], dtype=float)
y = np.array([1, 3, 7, 13, 21], dtype=float)
h = x[1] - x[0]
n = len(x) - 1


def build_diff_table(y):
    size = len(y)
    table = np.zeros((size, size))
    table[:, 0] = y
    for j in range(1, size):
        for i in range(size - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]
    return table


diff_table = build_diff_table(y)


def determine_degree(diff_table, tol=1e-9):
    size = diff_table.shape[0]
    for j in range(1, size):
        col = diff_table[:size - j, j]
        if np.allclose(col, 0, atol=tol):
            return j - 1
    return size - 1


degree = determine_degree(diff_table)


def newton_forward(x0, h, diff_table, xp):
    p = (xp - x0) / h
    result = diff_table[0][0]
    p_term, fact = 1.0, 1.0
    for k in range(1, diff_table.shape[0]):
        p_term *= (p - (k - 1))
        fact *= k
        result += (p_term / fact) * diff_table[0][k]
    return result


def newton_backward(xn, h, diff_table, xp):
    p = (xp - xn) / h
    size = diff_table.shape[0] - 1
    result = diff_table[size][0]
    p_term, fact = 1.0, 1.0
    for k in range(1, size + 1):
        p_term *= (p + (k - 1))
        fact *= k
        result += (p_term / fact) * diff_table[size - k][k]
    return result


def exact(v):
    
    return v**2 + v + 1


if __name__ == "__main__":
    print(f"Degree of interpolating polynomial: {degree}")
    f_forward = newton_forward(x[0], h, diff_table, 2.5)
    f_backward = newton_backward(x[-1], h, diff_table, 3.7)
    print(f"Forward  f(2.5) = {f_forward}  (exact {exact(2.5)})")
    print(f"Backward f(3.7) = {f_backward}  (exact {exact(3.7)})")