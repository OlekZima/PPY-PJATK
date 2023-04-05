import string

alphabet = list(string.ascii_uppercase * 2)


def ceaser(text_to_cypher, move_number, cypher=True):
    output_text = list(text_to_cypher)
    i = 0
    for letter in text_to_cypher:
        if letter == ' ' or letter == ',' or letter == '.' or letter == '!' or letter == '?':
            output_text[i] = letter
        else:
            output_text[i] = alphabet[
                alphabet.index(letter) + move_number if cypher else alphabet.index(letter) - move_number]
        i += 1
    return ''.join(output_text)


def main():
    print("""
    Wybierz jendą z opcji wpisując liczbę:
    1. Zaszyfrować
    2. Deszyfrować
    """)
    option = int(input("Wpisz liczbę: "))

    text = input("Podaj tekst: ")
    move_number = int(input("Podaj współczynnik przesunięcia: "))

    if option == 1:
        output = ceaser(text.upper(), move_number, cypher=True)
        print(f"Zaszyfrowana wiadomość to: {output}")
    elif option == 2:
        output = ceaser(text.upper(), move_number, cypher=False)
        print(f"Odszyfrowana wiadomość to: {output}")
    else:
        print("Niepoprawna opcja")


main()
