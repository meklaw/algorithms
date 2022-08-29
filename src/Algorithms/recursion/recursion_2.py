def sum_of_nums(num: int):
    if num == 0:
        return 0
    if num < 0:
        num = -num
    return num % 10 + sum_of_nums(num//10)