bin_number = int((input("Podaj liczbę w systemie dwójkowym: ")), 2)
oct_number = int(input("Podaj liczbę w systemie ósemkowym: "), 8)
hex_number = int(input("Podaj liczbę w systemie szestnaskowym: "), 16)

print(
    f"Zmienna bin_number zawiera liczbę {bin(bin_number)} zapisaną w systemie dwójkowym, a po konwersji na system "
    f"dziesiętny je wartość wynosi {bin_number}.\n")

print(
    f"Zmienna oct_number zawiera liczbę {oct(oct_number)} zapisaną w systemie ósemkowym, a po konwersji na system "
    f"dziesiętny je wartość wynosi {oct_number}.\n")

print(
    f"Zmienna hex_number zawiera liczbę {hex(hex_number)} zapisaną w systemie szestnastkowym, a po konwersji na "
    f"system dziesiętny je wartość wynosi {hex_number}.\n")
