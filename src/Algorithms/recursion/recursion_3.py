def len_of_list(array: list):
    try:
        array.pop()
    except IndexError:
        return 0
    return len_of_list(array) + 1
