def find_max(array: list):
    if len(array) < 2:
        return None
    first_max = array.pop()
    second_max = array.pop()
    if second_max > first_max:
        replace = first_max
        first_max = second_max
        second_max = replace

    return find_max_recursion(array, first_max, second_max)


def find_max_recursion(array: list, first_max, second_max):
    if len(array) == 0:
        return second_max
    element = array.pop()
    if element >= first_max:
        second_max = first_max
        first_max = element
    return find_max_recursion(array, first_max, second_max)
