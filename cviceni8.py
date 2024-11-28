def obvod_ctverce(delka_strany):
    # funkce vypocita obvod ctverce z delky jeho strany
    return 4 * delka_strany


def obsah_ctverce(delka_strany):
    # funkce vypocita obsah ctverce z delky jeho strany
    return delka_strany ** 2


def pocet_pismen(text, pismeno):
    # funkce vrati pocet vyskytu pismene v textu
    pocet = 0
    for p in text:
        if p == pismeno:
            pocet += 1
    return pocet


def index_pismene(text, pismeno):
    # funkce vrati indexy daneho pismene v textu, tzn. pro text="ahoj, honzo" a pismeno="h" vrati [1, 6]
    return []


if __name__ == "__main__":
    print(obsah_ctverce(5))
    print(obsah_ctverce(5))