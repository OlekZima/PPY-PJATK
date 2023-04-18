def add_product(products):
    name = input("Podaj nazwę produktu: ")
    price = float(input("Podaj cenę produktu: "))
    products[name] = price
    print(f"Dodano produkt {name} o cenie {price} zł")


def remove_product(products):
    name = input("Podaj nazwę produktu do usunięcia: ")
    if name in products:
        del products[name]
        print(f"Usunięto produkt {name}")
    else:
        print(f"Produkt {name} nie istnieje w bazie")


def list_products(products):
    print("Lista produktów w bazie:")
    for name, price in products.items():
        print(f"{name} - {price} zł")


def search_product(products):
    name = input("Podaj nazwę produktu do wyszukania: ")
    if name in products:
        print(f"Znaleziono produkt {name} o cenie {products[name]} zł")
    else:
        print(f"Nie znaleziono produktu {name} w bazie")


def main():
    products = {}
    while True:
        print("""
Wybierz opcję:
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl listę produktów
4. Wyszukaj produkt
5. Wyjście
        """)
        choice = input("Twój wybór: ")
        if choice == '1':
            add_product(products)
        elif choice == '2':
            remove_product(products)
        elif choice == '3':
            list_products(products)
        elif choice == '4':
            search_product(products)
        elif choice == '5':
            print("Koniec programu")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie")


main()
