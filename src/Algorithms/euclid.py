def euclidGCD(a: int, b: int):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return euclidGCD(a % b, b)

    return euclidGCD(b % a, a)
