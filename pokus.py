import sys

def main(soubor):
    otevreny_soubor = open(soubor, "r")
    for radka in otevreny_soubor:
        parametry = radka.split(",")
        vek = int(parametry[2])
        if vek > 20:
            print(radka)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Zadej nazev souboru")
        sys.exit(1)
    soubor = sys.argv[1]
    main(soubor)
