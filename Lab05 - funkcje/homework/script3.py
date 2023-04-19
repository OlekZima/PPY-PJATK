import random

# Przykładowe dane
male_litery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
duze_litery = [lit.upper() for lit in male_litery]
cyfry = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Wybieranie znaków zgodnie z zadanymi kryteriami
male_wybrane = [lit for idx, lit in enumerate(male_litery) if idx % 2 == 0 or idx % 5 == 0]
duze_wybrane = [lit for idx, lit in enumerate(duze_litery[::-1]) if idx % 2 == 0 and idx % 3 == 0]
cyfry_wybrane = [cyfry[idx] if idx % 2 == 0 else cyfry[-(idx + 1)] for idx in range(len(cyfry))]


def generuj_haslo(poziom_trudnosci):
    if poziom_trudnosci == "łatwe":
        znaki = random.choice([male_wybrane, duze_wybrane, cyfry_wybrane])
    elif poziom_trudnosci == "średnie":
        znaki = random.choice([male_wybrane + duze_wybrane, male_wybrane + cyfry_wybrane, duze_wybrane + cyfry_wybrane])
    elif poziom_trudnosci == "trudne":
        znaki = male_wybrane + duze_wybrane + cyfry_wybrane
    else:
        raise ValueError("Nieprawidłowy poziom trudności")

    return ''.join(random.sample(znaki, 8))


def generuj_hasla(poziom_trudnosci, liczba_hasel):
    hasla = []
    for _ in range(liczba_hasel):
        hasla.append(generuj_haslo(poziom_trudnosci))
    return hasla


# Przykład użycia
poziom_trudnosci = "średnie"
hasla = generuj_hasla(poziom_trudnosci, 10)
print(hasla)
