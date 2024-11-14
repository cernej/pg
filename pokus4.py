class Zvire:
    def __init__(self, barva):
        self.barva = barva
    
    def vrat_bravu(self):
        return self.barva

    def zvuk(self):
        return "Zvire vydava zvuk"


class Pes(Zvire):
    def __init__(self, barva, rasa):
        super().__init__(barva)
        self.rasa = rasa
    
    def zvuk(self):
        return "Steka"


class Kocka(Zvire):
    def __init__(self, barva):
        super().__init__(barva)


if __name__ == "__main__":

    pes1 = Pes("hnedy", "jezevcik")
    pes2 = Pes("cerny", "ovcak")
    kocka1 = Kocka("bila")

    print(pes1.zvuk())
    print(pes2.zvuk())
    print(kocka1.zvuk())