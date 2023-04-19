"""
Dziedziczenie
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

    # nadpisuje zmienną specjalną (zmiania działanie polecenia print)
    def __str__(self):
        return self.gatunek + " ma " + str(self.wiek) + " lat i osiąga prędkość " + str(self.max_predkosc) + " km/h"


class Ptak(Zwierz):
    def __init__(self, gatunek, wiek, predkosc, max_predkosc_lotu, miejsce):
        # funkcja super() zwraca klasę Zwierz
        super().__init__(gatunek, wiek, predkosc)
        self.predkosc_lotu = max_predkosc_lotu
        self.miejsce = miejsce

    def przenies(self):
        if self.miejsce == "klatka":
            self.miejsce = "otwarty"
        else:
            self.miejsce = "klatka"


# deklaracja instancji klasy
p = Ptak("pingwin", 2, 3, 0, "otwarty")
print(p)

p.przenies()
print(p.miejsce)

p.przenies()
print(p.miejsce)
