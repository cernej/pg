def my_enumerate(iterable, start=0):
    """
    Nase vlastni implementace enumerate()
    """
    results = []
    index = start
    for value in iterable:
        results.append( (index, value) )
        index += 1
    return results


def while_enumerate(iterable, start=0):
    results = []
    i = 0
    while i < len(iterable):
        results.append( (start + i, iterable[i]) )
        i += 1
    return results


if __name__ == "__main__":

    seznam = list(enumerate(["ahoj", "cau", "jak", "se", "mas"], 2))
    print(seznam)

    seznam = while_enumerate(["ahoj", "cau", "jak", "se", "mas"], 2)
    print(seznam)

    # for i, hodnota in seznam:
    #     print(f'Slovo {hodnota} je na {i}. pozici')