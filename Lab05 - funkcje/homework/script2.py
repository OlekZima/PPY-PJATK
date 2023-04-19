sklepy = ["Sklep 1", "Sklep 2", "Sklep 3", "Sklep 4", "Sklep 5"]
produkty = [
    {"nazwa": "Produkt 1", "producent": "Producent A", "data_waznosci": "2023-06-10", "kategoria": "Jedzenie"},
    {"nazwa": "Produkt 2", "producent": "Producent B", "data_waznosci": "2023-08-15", "kategoria": "Napoje"},
    {"nazwa": "Produkt 3", "producent": "Producent C", "data_waznosci": "2023-07-05", "kategoria": "Przyprawy"},
    {"nazwa": "Produkt 4", "producent": "Producent A", "data_waznosci": "2023-05-23", "kategoria": "Jedzenie"},
    {"nazwa": "Produkt 5", "producent": "Producent B", "data_waznosci": "2023-12-30", "kategoria": "Napoje"}
]
ceny = [10, 15, 5, 20, 12]
klienci = ["Klient 1", "Klient 2", "Klient 3", "Klient 4", "Klient 5"]
kupione_produkty = []

# 1
sklepy_produkty = []
for idx_sklep, sklep in enumerate(sklepy):
    if idx_sklep % 2 != 0:
        for idx_produkt, produkt in enumerate(produkty):
            if idx_produkt % 2 == 0 and idx_produkt % 3 == 0:
                sklepy_produkty.append((sklep, produkt["nazwa"]))

print(sklepy_produkty)

# 2
produkty_klientow = {}
for idx_klient, klient in enumerate(klienci):
    produkty_klientow[klient] = []
    for idx_produkt, produkt in enumerate(produkty):
        if idx_produkt % (idx_klient + 1) == 0:
            produkty_klientow[klient].append(produkt["nazwa"])

print(produkty_klientow)

# 3
produkty_ceny = {}
for idx, produkt in enumerate(produkty):
    produkty_ceny[produkt["nazwa"]] = ceny[-(idx + 1)]

print(produkty_ceny)
