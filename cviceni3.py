def my_range(start, stop, step=1):
    """
    Nase vlastni implementace range(), chceme, aby se chovala uplne stejne jako range
    """
    result = []
    value = start
    while value < stop:
        result.append(value)
        value += step
    return result


def my_enumerate(iterable, start=0):
    """
    Nase vlastni implementace enumerate()
    """
    result = []
    index = start
    for value in iterable:
        result.append((index, value))
        index += 1
    return result

def while_enumerate(iterable, start=0):
    result = []
    i = 0
    while i < len(iterable):
        result.append(  ( i+start, iterable[i] )  )
        i += 1
    return result


def my_zip(*iterables):
    """
    iterables = [
    [1,    2,   3],
    [4,    5,   6],
    [7,    8,   9],
    ["a", "b", "c"]
    ]
    iterables[2][1]
    ->
    [
    [1, 4, 7, "a"],
    [2, 5, 8, "b"],
    [3, 6, 9, "c"]
    ]
    """
    results = []
    lenght = len(iterables[0])
    for i in range(0, lenght):
        subresult = []
        for j in range(0, len(iterables)):
            subresult.append(iterables[j][i])
        results.append(tuple(subresult))

    return results


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
