def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    nact = {11: "jedenact", 12: "dvanact"}
    desitky = {1: "deset", 2: "dvacet", 3: "tricet"}
    jednoty = {1: "jedna", 2: "dva", 3: "tri"}
    cislo = int(cislo)
    if cislo == 0:
        return "nula"
    elif cislo == 100:
        return "sto"
    elif cislo >= 11 and cislo <= 19:
        return nact[cislo]
    else:
        d = cislo // 10
        j = cislo % 10
        vysledek = desitky[d]
        if j != 0:
            vysledek += " " + jednoty[j]
        return vysledek


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)