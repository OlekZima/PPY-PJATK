"""
Lab02 - operacja na łańcuchach i konwersja typów
"""
napis = "Wiek: " + str(10)
print(napis)

# Zamiana znaków w tekście
print(napis.replace("W", "w"))

print(napis.lower())
print(napis.upper())

# Konwersja typu tekstowego na typ liczbowy
a = "5"
b = 7
print(int(a) + b)

# kowersja typu liczbowego na typ tekstowy
a = '6'
b = 9
print(a + repr(b))
print(a + str(b))
