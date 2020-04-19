from tabulate import tabulate
from operator import mul

M = 5
X_1 = [
    0.359, 0.646, 0.652, 1.303, 1.888, 4.351, 4.564, 5.066, 5.089, 5.329,
    5.739, 5.763, 5.954, 6.338, 6.511, 6.716, 7.038, 8.211, 8.606, 8.689,
    9.682, 9.901, 10.490, 11.243, 11.569, 12.063, 13.995, 17.387, 17.723, 19.335
    ]

def sumiX(X):
    return sum(list(map(mul, X, list(range(1, len(X) + 1)))))

def check_convergence(X, N):
    A = sumiX(X) / sum(X)
    if A <= (N + 1) / 2:
        print("Не сходится ( A =", A, "<=", ((N + 1) / 2), ")")
        return A
    else:
        print("B существует ( A =", A, ">", ((N + 1) / 2), ")")
        return A

def solveB(N, M, A):
    m_list = list(range(N + 1, M + 1))
    f_list = list(
        map(lambda m: sum(
            map(lambda i: 1 / (m - i), range(1, N + 1))
        ), m_list))
    g_list = list(map(lambda m: N / (m - A), m_list))
    abs_list = list(map(lambda f, g: abs(f - g), f_list, g_list))
    print(tabulate([
        ["m"] + m_list,
        ["f"] + f_list,
        ["g"] + g_list,
        ["|f - g|"] + abs_list
    ]))
    m_fg = abs_list[0]
    m_idx = 1
    for i in range(0, len(abs_list) - 1):
        if m_fg < abs_list[i + 1]:
            break
        m_fg = abs_list[i + 1]
        m_idx = abs_list.index(m_fg) + 1
    m = N + m_idx
    B = m - 1
    print("m =", m, " (|f - g| =", m_fg, " idx =", m_idx, ") =>")
    print("B =", B)
    return B

def solveK(X, B):
    K = len(X) / ((B + 1) * sum(X) - sumiX(X))
    print("K =", K)
    return K

def print_input(X, N, M):
    print("=====================ИСХОДНЫЕ ДАННЫЕ=======================")
    print("N =", N, " M =", M)
    i_list = list(range(1, N + 1))
    rows = N // 10
    if N % rows != 0:
        rows += 1
    table = []
    for row in range(0, rows):
        table += [ ["i"] + i_list[row * 10:(row + 1) * 10], ["X_i"] + X[row * 10:(row + 1) * 10] ]
    print(tabulate(table))

def solve_jelinski_moranda(X, M):
    n = len(X)
    m = n + M
    print_input(X, n, m)
    print("=========================РЕШЕНИЕ===========================")
    B = solveB(n, m, check_convergence(X, n))
    K = solveK(X, B)
    X_ave = list(map( lambda n: 1 / (K * (B - n)), range(n, B)))
    print("===========================================================")
    print("Таблица со средним временем до нахождения последней ошибки:")
    print(tabulate([list(range(n + 1, B + 1)),
                   ["X_ave"] + X_ave],
                   headers="firstrow"))
    print("===========================================================")
    X_overall = sum(X) + sum(X_ave)
    print("Полное время:", X_overall)

solve_jelinski_moranda(X_1, M)


