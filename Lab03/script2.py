"""
Lab03 - krotki
"""

# Tworzenie krotki
krotka1 = ()
print(krotka1)

krotka1 = 1,
print(krotka1)

krotka1 = (1,)
print(krotka1)

krotka2 = 1, 3.14, "pjatk"
print(krotka2)

krotka3 = (1, 3.14, [2, 3], 1)
print(krotka3)

napis = "abcdefgh"
print(tuple(napis))

# Indeksowanie krotek
print(krotka3[0])
print(krotka3[:2])

# Operacje na krotkach
print(krotka3.count(1))
print(krotka3.index(1))
print(krotka3.index(3.14))
