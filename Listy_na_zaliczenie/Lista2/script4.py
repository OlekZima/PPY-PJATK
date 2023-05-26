import datetime


# Funkcja do generowania unikalnego tokena
def generate_token(first_name, last_name, email, expiration_date):
    # Kombinacja danych użytkownika w celu utworzenia ciągu
    data = first_name + last_name + email + expiration_date

    # Generowanie unikalnego tokenu na podstawie ciągu danych
    token = ""
    for char in data:
        token += str(ord(char))

    return token


# Funkcja do weryfikacji tokena
def verify_token(token, first_name, last_name, email, expiration_date):
    # Generowanie oczekiwanego tokenu na podstawie podanych danych
    expected_token = generate_token(first_name, last_name, email, expiration_date)

    # Porównanie podanego tokenu z oczekiwanym tokenem
    if token == expected_token:
        return True
    else:
        return False


# Przykładowe dane użytkownika
first_name = input("Podaj imię: ")
last_name = input("Podaj nazwisko: ")
email = input("Podaj adres e-mail: ")
expiration_date = input("Podaj datę ważności tokena (RRRR-MM-DD): ")

# Wygenerowanie tokenu
token = generate_token(first_name, last_name, email, expiration_date)
print("Wygenerowany token:", token)

# Weryfikacja tokenu
user_token = input("Podaj token do weryfikacji: ")
is_valid = verify_token(user_token, first_name, last_name, email, expiration_date)

# Sprawdzenie ważności tokenu
if is_valid:
    print("Token jest ważny. Dostęp przyznany.")
    # Tutaj można użyć tokenu do uzyskania danych użytkownika
else:
    print("Token jest nieprawidłowy. Dostęp zabroniony.")
