def pobierz_indeksy():
    indeks_kategorii = int(input("Podaj indeks kategorii (0-2): "))
    indeks_slowa = int(input("Podaj indeks słowa (0-2): "))
    return indeks_kategorii, indeks_slowa


def wybierz_kategorie_slowo(kategorie, slowa, indeks_kategorii, indeks_slowa):
    kategoria = kategorie[indeks_kategorii]
    slowo = slowa[indeks_kategorii][indeks_slowa].lower()
    return kategoria, slowo


def wyswietl_kategorie_i_slowo(kategoria, slowo):
    print("Kategoria:", kategoria)
    print(" ".join("_" for _ in slowo))


def graj(kategoria, slowo):
    punkty = {"Gracz1": 0, "Gracz2": 0}
    ukryte_slowo = ["_"] * len(slowo)
    zgadniete = False

    while not zgadniete:
        for gracz in ["Gracz1", "Gracz2"]:
            litera = input(f"{gracz}, podaj literę lub zgadnij całe słowo: ").lower()

            if litera == slowo:
                nieodkryte_litery = ukryte_slowo.count("_")
                ukryte_slowo = list(slowo)
                zgadniete = True
                print(f"WYGRYWA {gracz.upper()}!!!")
                punkty[gracz] += nieodkryte_litery * 2
                break

            elif len(litera) == 1 and litera in 'abcdefghijklmnopqrstuvwxyz':
                if litera in slowo:
                    for i, l in enumerate(slowo):
                        if l == litera:
                            ukryte_slowo[i] = litera
                            punkty[gracz] += 1

                    print(" ".join(ukryte_slowo))

                    if "".join(ukryte_slowo) == slowo:
                        zgadniete = True
                        print(f"WYGRYWA {gracz.upper()}!!!")
                        break

                else:
                    print("Nie ma takiej litery.")
            else:
                print("Niepoprawna litera lub słowo.")
    return punkty


def wyswietl_wyniki(punkty):
    print("\n#############################\nPunkty\n#############################")
    for gracz, pkt in punkty.items():
        print(f"{gracz}: {pkt}")


def main():
    kategorie = ["Zwierzęta", "Kraje", "Filmy"]
    slowa = [
        ["kot", "wieloryb", "koń"],
        ["Polska", "Niemcy", "Włochy"],
        ["Incepcja", "Matrix", "Avatar"]
    ]

    indeks_kategorii, indeks_slowa = pobierz_indeksy()
    kategoria, slowo = wybierz_kategorie_slowo(kategorie, slowa, indeks_kategorii, indeks_slowa)
    wyswietl_kategorie_i_slowo(kategoria, slowo)
    punkty = graj(kategoria, slowo)
    wyswietl_wyniki(punkty)


main()
