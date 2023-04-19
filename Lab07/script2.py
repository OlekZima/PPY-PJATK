"""Inicializowanie klas i atrybuty klas"""


class Zwierz:
    """Pierwsza klasa"""
    rodzaj = "zwierzę"

    def __init__(self, gatunek, wiek):
        self.gatunek = gatunek
        self.wiek = wiek

    def podaj_gatunek(self):
        print("lis")


a = Zwierz("lis", 5)
b = Zwierz("python", 2)

print(a.gatunek, a.wiek)
print(b.gatunek, b.wiek)

b.dlugosc = 10
print(b.dlugosc)
# print(a.dlugosc)

print(a.rodzaj, b.rodzaj)

b.dlugosc = 11
print(b.dlugosc)
a.wiek = 6
print(a.wiek)

# atrybuty specjalne - nie wymagają deklaracji

# atrybuty klasy w formie słownika
print(a.__dict__)
print(b.__dict__)

# opis klasy
print(Zwierz.__doc__)
print(a.__doc__)
