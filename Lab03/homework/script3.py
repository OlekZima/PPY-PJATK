size = int(input("Podaj rozmiar tabliczki: "))

for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(i * j, end=' ')
    print(end='\n')
