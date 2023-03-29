start = int(input("Podaj początek przedziału: "))
stop = int(input("Podaj koniec przedziału: "))

if start < stop:
    for i in range(start, stop + 1):
        print(i)
else:
    for i in range(start, stop - 1, -1):
        print(i)
