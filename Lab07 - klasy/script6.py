"""
Polimorfizm - przesłanianie metod klasy nadrzędnej. Metody prywatne
"""


class Zwierz:
    """Pierwsza klasa"""
    rodzaj = "zwierzę"
    zwierzeta = {}

    def __init__(self, gatunek, wiek, predkosc, stan_zdrowia):
        self.gatunek = gatunek
        self.wiek = wiek
        self.max_predkosc = predkosc
        self.stan_zdrowia = stan_zdrowia

        if gatunek in Zwierz.zwierzeta:
            Zwierz.zwierzeta[gatunek] += 1
        else:
            Zwierz.zwierzeta[gatunek] = 1

    def _sprawdz_stan_zdrowia(self):
        if self.stan_zdrowia == 1:
            return 1
        else:
            return 0

    def oblicz_odleglosc(self, czas):
        print(czas * self.max_predkosc)

    @staticmethod
    def wypisz_zwierzeta():
        print(Zwierz.zwierzeta)

    # nadpisywanie zmienną specjalną (zmienia działania polecenia print()
    def __str__(self):
        return f"{self.gatunek} ma {self.wiek} lat i osiąga prędkość {self.max_predkosc} km/h."


class Ptak(Zwierz):
    def __init__(self, gatunek, wiek, predkosc, stan_zdrowia, max_predkosc_lotu, miejsce):
        super().__init__(gatunek, wiek, predkosc, stan_zdrowia)
        self.predkosc_lotu = max_predkosc_lotu
        self.miejsce = miejsce

    def przenies(self):
        if self.miejsce == "klatka" and self._sprawdz_stan_zdrowia() == 1:
            self.miejsce = "otwarty"
        else:
            self.miejsce = "klatka"

    def oblicz_odleglosc(self, czas):
        if self.predkosc_lotu == 0:
            print(czas * self.max_predkosc)
        else:
            print(czas * self.predkosc_lotu)


p = Ptak("pingwin", 2, 3, 1, 0, "otwarty")
p1 = Ptak("kos", 2, 2, 0, 15, "klatka")

# odleglosc w h
p.oblicz_odleglosc(2)
p1.oblicz_odleglosc(2)

# metody prywatne
p.przenies()
print(p.miejsce)

p1.przenies()
print(p.miejsce)
