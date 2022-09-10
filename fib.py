import numpy as np

A = np.array([
    [0, 1],
    [1, 1]
])


def fib(n):
    if n == 0:
        return 1

    if n == 1:
        return 1

    x = np.matmul([1, 1], np.linalg.matrix_power(A, n - 1))

    return x[-1]


def fib2(n):
    if n == 0:
        return 1

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


print(fib2(150))
