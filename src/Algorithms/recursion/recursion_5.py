def print_even_elements(array: list):
    try:
        element = array.pop()
        if element % 2 == 0:
            print(element)
    except IndexError:
        return
    except TypeError:
        pass
    print_even_elements(array)
