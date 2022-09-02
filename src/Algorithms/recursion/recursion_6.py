def print_every_second(array: list):
    if len(array) < 2:
        return
    array.pop(0)
    print(array.pop(0))
    print_every_second(array)
