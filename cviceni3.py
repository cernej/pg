def my_range(start, stop, step=1):
    """
    Nase vlastni implementace range(), chceme, aby se chovala uplne stejne jako range
    """
    pass

def my_enumerate(iterable, start=0):
    """
    Nase vlastni implementace enumerate()
    """
    pass

def while_enumerate(iterable, start=0):
    pass

def my_zip(*iterables):
    pass


if __name__ == "__main__":

    # print(list(range(1, 10)))
    # print(my_range(1, 10, 3))

    # print(list(enumerate("abcdef", 2)))
    # print(while_enumerate("abcdef", 2))

    # print(list(enumerate(['Alice', 'Bob', 'Eva'])))
    # print(my_enumerate(['Alice', 'Bob', 'Eva']))

    my_zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"])

    print(list(zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"])))
    print(my_zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"]))
