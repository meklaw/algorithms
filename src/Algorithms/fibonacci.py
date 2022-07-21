def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


def fib_digit(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = (a + b) % 10
        a = b
        b = c
    return b


def fib_mod(n: int, m: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = [0, 1]
    for i in range(2, n + 1):
        a.append((a[i - 1] + a[i - 2]) % m)
        if a[i - 1] == 0 and a[i] == 1:
            return a[n % (i - 1)]
    return n % m
