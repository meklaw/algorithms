def power(num, num_to_degree: int):
    if num_to_degree == 0:
        return 1
    if num_to_degree < 0:
        return 1 / power(num, -num_to_degree)
    return num * power(num, num_to_degree - 1)
