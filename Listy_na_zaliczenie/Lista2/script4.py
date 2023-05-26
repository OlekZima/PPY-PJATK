def generate_token(first_name, last_name, email, expiration_date):
    data = first_name + last_name + email + expiration_date

    token = ""
    for char in data:
        token += str(ord(char))

    return token


def verify_token(token, first_name, last_name, email, expiration_date):
    expected_token = generate_token(first_name, last_name, email, expiration_date)

    if token == expected_token:
        return True
    else:
        return False


first_name = input("Podaj imię: ")
last_name = input("Podaj nazwisko: ")
email = input("Podaj adres e-mail: ")
expiration_date = input("Podaj datę ważności tokena (RRRR-MM-DD): ")

token = generate_token(first_name, last_name, email, expiration_date)
print("Wygenerowany token:", token)

user_token = input("Podaj token do weryfikacji: ")
is_valid = verify_token(user_token, first_name, last_name, email, expiration_date)

if is_valid:
    print("Token jest ważny. Dostęp przyznany.")
else:
    print("Token jest nieprawidłowy. Dostęp zabroniony.")
