import sys

def main(soubor):
    otevreny_soubor = open(soubor, "r")
    for radek in otevreny_soubor:
        casti = radek.split(",")
        vek = int(casti[2])
        if vek < 20:
            print(radek)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Zadej soubor")
        sys.exit(1)
    main(sys.argv[1])
