def print_even_elements(array: list):
    if len(array) == 0:
        return
    try:
        element = array.pop()
        if element % 2 == 0:
            print(element)
    except TypeError:
        pass
    print_even_elements(array)
