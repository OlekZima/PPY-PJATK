produkty = {}


def dodaj_produkt(nr, nazwa, ilosc, cena):
    produkty[nr] = {'nazwa': nazwa, 'ilosc': ilosc, 'cena': cena}


def usun_produkt(nr):
    del produkty[nr]


def wyswietl_produkty():
    print("Nr  |  Nazwa produktu  |  Ilość  |  Cena")
    for nr, produkt in produkty.items():
        print(f"{nr}  |  {produkt['nazwa']}  |  {produkt['ilosc']}  |  {produkt['cena']} zł")


def zmien_produkt(nr, nazwa, ilosc, cena):
    produkty[nr] = {'nazwa': nazwa, 'ilosc': ilosc, 'cena': cena}


dodaj_produkt(1, 'Jajka', 10, 2.50)
dodaj_produkt(2, 'Chleb', 1, 3.20)
wyswietl_produkty()
zmien_produkt(1, 'Jajka ekologiczne', 12, 3.00)
usun_produkt(2)
wyswietl_produkty()
