"""
Metody klas
"""


class Zwierz:
    """Pierwsza klasa"""
    rodzaj = "zwierzę"
    zwierzeta = {}

    def __init__(self, gatunek, wiek, predkosc):
        self.gatunek = gatunek
        self.wiek = wiek
        self.max_preskosc = predkosc
        if gatunek in Zwierz.zwierzeta:
            Zwierz.zwierzeta[gatunek] += 1
        else:
            Zwierz.zwierzeta[gatunek] = 1

    def oblicz_odleglosc(self, czas):
        print(czas * self.max_preskosc)

    @staticmethod
    def wypisz_zwierzeta():
        print(Zwierz.zwierzeta)


Zwierz.wypisz_zwierzeta()

# instancje klas (inicjalizacja obiektów)
a = Zwierz("lis", 5, 10)
b = Zwierz("python", 2, 5)
c = Zwierz("lis", 3, 10)

a.oblicz_odleglosc(2)
b.oblicz_odleglosc(2)

# definiowanie metod na poziomie klas
Zwierz.wypisz_zwierzeta()
