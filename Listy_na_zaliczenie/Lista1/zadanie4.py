ceny_przed = [3.69, 4.5, 3.6, 4.0, 3.99, 3.59]
ceny_po = [4.5, 5.5, 4.69, 4.99, 4.00]

print('Najwyższa cena po nałożeniu podatku: ', max(ceny_po))
print('Najniższa cena przed nałożeniem podatku: ', min(ceny_przed))
print('Najniższa cena po nałożeniem podatku: ', min(ceny_po))
print('Średnia cena przed nałożeniem podatku: ', sum(ceny_przed) / len(ceny_przed))
print('Średnia cena po nałożeniu podatku: ', sum(ceny_po) / len(ceny_po))
