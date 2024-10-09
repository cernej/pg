# funkce vypise "Číslo X je sudé" pokud je cislo sude a "Číslo X je liché" pokud je cislo liche
def sudy_nebo_lichy(cislo):
    if cislo % 2:
        print("Číslo", cislo, "je liché")
    else:
        print("Číslo", cislo, "je sudé")

if __name__ == "__main__":
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)
