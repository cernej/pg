def je_tah_mozny_pesec(cilova_pozice, aktualni_pozice, obsazene_pozice):
    # pokud se jedna o jiny sloupec, vrat False
    if aktualni_pozice[1] != cilova_pozice[1]:
        return False
    # pokud se pesak posune o 1 pole dopredu, vrat True
    if aktualni_pozice[0] + 1 == cilova_pozice[0]:
        return True
    # pokud je pesak na radku 2 a posune se o 2 pole dopredu a neni obsazeno pole po ceste, vrat True
    return aktualni_pozice[0] == 2 \
        and aktualni_pozice[0] + 2 == cilova_pozice[0] \
        and (aktualni_pozice[0] + 1, aktualni_pozice[1]) in obsazene_pozice


def je_tah_mozny_jezdec(cilova_pozice, aktualni_pozice, obsazene_pozice):
    for i in [1, 2]:
        if abs(aktualni_pozice[0] - cilova_pozice[0]) == 1 and abs(aktualni_pozice[1] - cilova_pozice[1]) == 2:
            return True
        if abs(aktualni_pozice[0] - cilova_pozice[0]) == 2 and abs(aktualni_pozice[1] - cilova_pozice[1]) == 1:
            return True
    return False


def je_tah_mozny_strelec(cilova_pozice, aktualni_pozice, obsazene_pozice):
    if abs(aktualni_pozice[0] - cilova_pozice[0]) != abs(aktualni_pozice[1] - cilova_pozice[1]):
        return False
    for i in range(1, abs(aktualni_pozice[0] - cilova_pozice[0])):
        if (aktualni_pozice[0] + i, aktualni_pozice[1] + i) in obsazene_pozice:
            return False
        elif (aktualni_pozice[0] + i, aktualni_pozice[1] - i) in obsazene_pozice:
            return False
        elif (aktualni_pozice[0] - i, aktualni_pozice[1] + i) in obsazene_pozice:
            return False
        elif (aktualni_pozice[0] - i, aktualni_pozice[1] - i) in obsazene_pozice:
            return False
    return True


def je_tah_mozny_vez(cilova_pozice, aktualni_pozice, obsazene_pozice):
    if aktualni_pozice[0] != cilova_pozice[0] and aktualni_pozice[1] != cilova_pozice[1]:
        return False
    if aktualni_pozice[0] >= cilova_pozice[0]:
        position_range = range(cilova_pozice[0], aktualni_pozice[0])
    else:
        position_range = range(aktualni_pozice[0], cilova_pozice[0])
    for i in position_range:
        if (i, aktualni_pozice[1]) in obsazene_pozice:
            return False
    if aktualni_pozice[1] >= cilova_pozice[1]:
        position_range = range(cilova_pozice[1], aktualni_pozice[1])
    else:
        position_range = range(aktualni_pozice[1], cilova_pozice[1])
    for i in position_range:
        if (aktualni_pozice[0], i) in obsazene_pozice:
            return False
    return True


def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    if cilova_pozice in obsazene_pozice:
        return False
    
    aktualni_pozice = figurka["pozice"]
    if figurka["typ"] == "pěšec":
        return je_tah_mozny_pesec(cilova_pozice, aktualni_pozice, obsazene_pozice)
    elif figurka["typ"] == "jezdec":
        return je_tah_mozny_jezdec(cilova_pozice, aktualni_pozice, obsazene_pozice)
    elif figurka["typ"] == "věž":
        return je_tah_mozny_vez(cilova_pozice, aktualni_pozice, obsazene_pozice)
    elif figurka["typ"] == "střelec":
        return je_tah_mozny_strelec(cilova_pozice, aktualni_pozice, obsazene_pozice)
    elif figurka["typ"] == "dáma":
        if je_tah_mozny_vez(cilova_pozice, aktualni_pozice, obsazene_pozice) or je_tah_mozny_strelec(cilova_pozice, aktualni_pozice, obsazene_pozice):
            return True
    elif figurka["typ"] == "král":
        if abs(aktualni_pozice[0] - cilova_pozice[0]) <= 1 and abs(aktualni_pozice[1] - cilova_pozice[1]) <= 1:
            return True
    # Implementace pravidel pohybu pro různé figury zde.
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat
    print()
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici
    print()
    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
    print()
    print(je_tah_mozny(strelec, (1, 8), obsazene_pozice))  # True