def print_every_second(array: list):
    try:
        array.pop(0)
        print(array.pop(0))
    except IndexError:
        return
    print_every_second(array)
