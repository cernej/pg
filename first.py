# funkce vypise "Číslo X je sudé" pokud je cislo sude a "Číslo X je liché" pokud je cislo liche
def sudy_nebo_lichy(cislo):
    if cislo % 2:
        return "liche"
    else:
        return "sude"

def main():
    promena = 1
    vysledek = sudy_nebo_lichy(promena)

if __name__ == "__main__":
    main()