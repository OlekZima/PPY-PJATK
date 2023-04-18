def pitagorejska(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

if pitagorejska(a, b, c):
    print("Podane liczby spełniają twierdzenie pitagorejskie")
else:
    print("Podane liczby nie spełniają twierdzenia pitagorejskiego")

