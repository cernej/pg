def dec_to_bin2(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"
    cislo = int(cislo)
    if cislo == 0:
        return "0"
    pow = 0
    i = 0
    while True:
        m = 2 ** i
        if m > cislo:
            pow = i - 1
            break
    vysledek = ""
    for i in range(pow, -1, -1):
        m = 2 ** i
        if m <= cislo:
            vysledek += "1"
            cislo -= m
        else:
            vysledek += "0"
    return vysledek


def dec_to_bin(cislo):
    if cislo == 0:
        return "0"
    elif cislo == 1:
        return "1"
    else:
        return dec_to_bin(cislo // 2) + str(cislo % 2)


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"


if __name__ == "__main__":
    dec_to_bin(120)