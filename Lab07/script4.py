"""
Metody specjalne klas
"""


class Zwierz:
    """Pierwsza klasa"""
    rodzaj = "zwierzę"
    zwierzeta = {}

    def __init__(self, gatunek, wiek, predkosc):
        self.gatunek = gatunek
        self.wiek = wiek
        self.max_predkosc = predkosc

        if gatunek in Zwierz.zwierzeta:
            Zwierz.zwierzeta[gatunek] += 1
        else:
            Zwierz.zwierzeta[gatunek] = 1

    def oblicz_odleglosc(self, czas):
        print(czas * self.max_predkosc)

    @staticmethod
    def wypisz_zwierzeta():
        print(Zwierz.zwierzeta)

    # nadpisywanie zmienną specjalną (zmiania działanie polecenia print)
    def __str__(self):
        return self.gatunek + " ma " + str(self.wiek) + \
               " lat i osiąga prędkość " + str(self.max_predkosc) + " km/h"


a = Zwierz("lis", 3, 10)
print(a)
