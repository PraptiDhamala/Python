import numpy as np
# given data
X = np.array([0, 1, 2, 3, 4], dtype=float)
Y = np.array([1, 3, 7, 13, 21], dtype=float)
h = X[1] - X[0]
n = len(X) - 1
def build_diff_table(y):
    size = len(y)
    table = np.zeros((size, size))
    table[:, 0] = y
    for j in range(1, size):
        for i in range(size - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]
    return table
diff_table = build_diff_table(Y)
def print_forward_table(X, table):
    size = len(X)
    print("\nForward Difference Table")
    header = ["x", "y"] + [f"D^{k}y" for k in range(1, size)]
    print("".join(f"{h:<10}" for h in header))
    for i in range(size):
        row = [f"{X[i]:<10.1f}"]
        for j in range(size - i):
            row.append(f"{table[i][j]:<10.3f}")
        print("".join(row))
def print_backward_table(X, table):
    size = len(X)
    print("\nBackward Difference Table")
    header = ["x", "y"] + [f"grad^{k}y" for k in range(1, size)]
    print("".join(f"{h:<10}" for h in header))
    for i in range(size - 1, -1, -1):
        row = [f"{X[i]:<10.1f}"]
        for k in range(i + 1):
            row.append(f"{table[i - k][k]:<10.3f}")
        print("".join(row))
def print_central_table(X, table):
    size = len(X)
    mid = size // 2
    print(f"\nCentral Difference Table (centered about x = {X[mid]:.1f})")
    col_width = 12
    for order in range(size):
        entries = []
        for i in range(size - order):
            center_index = i + order / 2
            if abs(center_index - mid) <= (size - 1) / 2:
                entries.append((center_index, table[i][order]))
        row_str = "".join(
            f"{val:<{col_width}.3f}" for _, val in sorted(entries, key=lambda t: t[0])
        )
        print(f"Order {order}: {row_str}")
def determine_degree(table, tol=1e-9):
    size = table.shape[0]
    for j in range(1, size):
        col = table[: size - j, j]
        if np.allclose(col, 0, atol=tol):
            return j - 1
    return size - 1
def newton_forward(x0, h, table, xp):
    p = (xp - x0) / h
    result = table[0][0]
    p_term, fact = 1.0, 1.0
    for k in range(1, table.shape[0]):
        p_term *= (p - (k - 1))
        fact *= k
        result += (p_term / fact) * table[0][k]
    return result
def newton_backward(xn, h, table, xp):
    p = (xp - xn) / h
    size = table.shape[0] - 1
    result = table[size][0]
    p_term, fact = 1.0, 1.0
    for k in range(1, size + 1):
        p_term *= (p + (k - 1))
        fact *= k
        result += (p_term / fact) * table[size - k][k]
    return result
def exact_function(v):
    return v**2 + v + 1
def compare_results(label, xp, interpolated, exact_available=True):
    print(f"\n{label}")
    print(f"  x                 = {xp}")
    print(f"  Interpolated f(x) = {interpolated:.6f}")
    if exact_available:
        exact_val = exact_function(xp)
        error = abs(exact_val - interpolated)
        print(f"  Exact f(x)        = {exact_val:.6f}")
        print(f"  Absolute Error    = {error:.6e}")
    else:
        print("  Exact value not available.")
def main():
    print("=" * 60)
    print("Question 6: Finite Differences and Newton's Interpolation")
    print("=" * 60)
    print(f"X = {X}")
    print(f"Y = {Y}")
    print_forward_table(X, diff_table)
    print_backward_table(X, diff_table)
    print_central_table(X, diff_table)
    degree = determine_degree(diff_table)
    print(f"\nThe data represents a polynomial of degree {degree}.")
    f_forward = newton_forward(X[0], h, diff_table, 2.5)
    compare_results("Newton's Forward Interpolation Formula: f(2.5)", 2.5, f_forward)
    f_backward = newton_backward(X[-1], h, diff_table, 3.7)
    compare_results("Newton's Backward Interpolation Formula: f(3.7)", 3.7, f_backward)
    print("\n" + "-" * 65)
    print(f"{'Method':<22} | {'x':<6} | {'Interpolated':<14} | {'Exact':<10} | {'Error':<10}")
    print("-" * 65)
    print(f"{'Newton Forward':<22} | {2.5:<6} | {f_forward:<14.6f} | "
          f"{exact_function(2.5):<10.6f} | {abs(exact_function(2.5) - f_forward):<10.2e}")
    print(f"{'Newton Backward':<22} | {3.7:<6} | {f_backward:<14.6f} | "
          f"{exact_function(3.7):<10.6f} | {abs(exact_function(3.7) - f_backward):<10.2e}")
    print("-" * 65)
if __name__ == "__main__":
    main()