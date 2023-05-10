suma = 0
liczba = 1

while liczba <= 100:
    if liczba % 2 == 1:
        suma += liczba
    liczba += 1

print("Suma liczb nieparzystych w przedziale od 1 do 100 wynosi:", suma)
