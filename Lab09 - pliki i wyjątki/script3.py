"""
Lab09 - wyjątki
"""


def pobierz(sek, ind):
    return sek[ind]


pliki = ["czarny_kot.txt", "nowy_plik.txt"]
ind = 2

try:
    print(pobierz(pliki, ind))
except IndexError:
    print("Wystąpił błąd")

try:
    print(pobierz(pliki, ind))
except IndexError as e:
    print("Wystąpił błąd: ", e)
else:
    print("pobrano nazwę pliku")


pliki = ["czarny_kot.txt", "nowy_plik.txt"]
ind = 1

try:
    p = pobierz(pliki, ind)
    print(p)
    f = open(p)
except (IndexError, FileNotFoundError) as e:
    print("Wystąpił błąd: ", e)
else:
    print("pobrano nazwę pliku")

