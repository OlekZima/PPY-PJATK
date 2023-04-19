"""
Lab07 - klasy
"""


class Zwierz:
    """Pierwsza klasa"""

    def podaj_gatunek(self):
        print("lis")


a = Zwierz()
print(a)
b = Zwierz()
print(b)

# Sprawdzenie czy mamy do czynienia z tym samym obiektem
print(a == b)

# wywołanie metody obiektu

a.podaj_gatunek()
b.podaj_gatunek()
