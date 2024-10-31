import sys


class ChybaNeniCislo(Exception):
    pass


def vrat_data_ze_souboru(soubor):
    otevreny_soubor = open(soubor, "r")
    data = otevreny_soubor.read()
    try:
        cislo = int(data)
    except ValueError:
        raise ChybaNeniCislo
    return cislo


if __name__ == "__main__":

    try:
        soub = sys.argv[1]
        vysledek = vrat_data_ze_souboru(soub)
        print(vysledek)
    except IndexError:
        print("Zadej nazev soboru")
    except FileNotFoundError:
        print("Soubor neexistuje")
    except ChybaNeniCislo:
        print("Nase chyba neni cislo")