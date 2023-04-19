slowo_jeden = input("Podaj pierwsze słowo: ")
slowo_dwa = input("Podaj drugie słowo: ")

for char in slowo_jeden:
    if char in ["a", "ą", "e", "ę", "o", "ó", "i", "y", "u", "A", "Ą", "E", "Ę", "O", "Ó", "I", "Y", "U", "J", "j"]:
        slowo_jeden = slowo_jeden.replace(char, "7")

for char in slowo_dwa:
    if char in ["w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "v", "b", "n", "m", "W", "R", "T",
                "P", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "V", "B", "N", "M"]:
        slowo_dwa = slowo_dwa.replace(char, "6")

print((slowo_jeden + slowo_dwa).upper())
