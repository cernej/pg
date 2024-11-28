import sys
from knihovna import sudy_lichy


class Trida:
    def __init__(self, hodnota):
        self.atribut = hodnota


def funkce(parametr):
    promenna = str(parametr)
    return promenna


if __name__ == "__main__":
    argument = 50
    sudy_lichy(argument)
    if argument > 10:
        argument /= 2
    vysledek = funkce(argument)
    print(vysledek)

    polozky = [1,3,4,5,256]
    for i in polozky:
        x = i * 2
        print(x)
    
    i = 0
    while i < 10:
        print(i)
        i += 1