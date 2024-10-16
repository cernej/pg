def my_range(start, stop, step):
    """
    Nase vlastni implementace range(), chceme, aby se chovala uplne stejne jako range
    """
    return [0, 1, 2]


def my_enumerate(iterable):
    """
    Nase vlastni implementace enumerate()
    """
    return [(0, "a"), (1, "b"), (2, "c")]


def my_zip(*iterables):
    """
    Nase vlastni implementace zip()
    """
    return [(1,4,7), (2,5,8), (3,6,9)]


if __name__ == "__main__":

    print(list(range(1, 10)))
    print(my_range(1, 10, 1))

    print(list(enumerate("abcdef")))
    print(my_enumerate("abcdef"))

    print(list(zip([1,2,3], [4,5,6], [7,8,9], [10,11,12])))
    print(my_zip([1,2,3], [4,5,6], [7,8,9], [10,11,12]))
