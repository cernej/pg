def sudy_lichy(cislo):
    if cislo % 2:
        print("lichy")
    else:
        print("sudy")

def vypis_text():
    print("text")

if __name__ == "__main__":
    vstup = input("Zadej cislo")
    integer = int(vstup)
    sudy_lichy(integer)