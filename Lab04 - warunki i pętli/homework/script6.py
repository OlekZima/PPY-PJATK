start = int(input("Podaj początek przedziału: "))
stop = int(input("Podaj koniec przedziału: "))

suma = 0

for i in range(start, stop + 1):
    if (i+1) % 2 == 0:
        suma += i

print(f"Suma wynosi {suma}")
