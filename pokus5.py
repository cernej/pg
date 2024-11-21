class SouradniceError(Exception):
    pass

class Souradnice:
    def __init__(self, sirka, delka):
        self.__sirka = sirka
        self.__delka = delka
    
    @property
    def sirka(self):
        return self.__sirka

    @sirka.setter
    def sirka(self, nova_sirka):
        if nova_sirka < -180 or nova_sirka > 180:
            raise SouradniceError("Chybna sirka")
        self.__sirka = nova_sirka

    @property
    def delka(self):
        return self.__delka
    
    @delka.setter
    def delka(self, nova_delka):
        if nova_delka < -90 or nova_delka > 90:
            raise SouradniceError("Chybna delka")
        self.__delka = nova_delka

    def __str__(self):
        return f'{self.sirka}, {self.delka}'
    
    def __repr__(self):
        return f'Souradnice({self.sirka}, {self.delka})'
    

if __name__ == "__main__":
    s = Souradnice(1, 22)
    s.sirka = 20
    s.delka = 100
    print(s.sirka)
    print(s.delka)
    