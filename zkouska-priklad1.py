# vas program nacte ze souboru, ktery dostane jako argument z prikazove radky, text a vypise ho pozpatku
# vytvorte funkce pozpatku(), ktera jako parametr bere text a vraci ho pozpatku tzn "ahoj" -> "joha"
# osetrete chybove stavy pomoci try - except
import sys

# def pozpatku(text):
#     text_pozpatku = ""
#     for pismeno in reversed(text):
#         text_pozpatku += pismeno
#     return text_pozpatku


def pozpatku(text):
    text_pozpatku = ""
    i = len(text) - 1
    while i >= 0:
        pismeno = text[i]
        text_pozpatku += pismeno
        i -= 1
    return text_pozpatku


if __name__ == "__main__":
    try:
        soubor = sys.argv[1]
        with open(soubor, "r") as fp:
            obsah = fp.read()
            obracene = pozpatku(obsah)
            print(obracene)
    except IndexError:
        print("Zadej nazev souboru")
    except FileNotFoundError:
        print("Soubor neexistuje")
