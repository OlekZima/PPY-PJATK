import datetime
import uuid


def generate_token(first_name, last_name, email, expiration_date):
    data = first_name + last_name + email + expiration_date
    token = str(uuid.uuid5(uuid.NAMESPACE_DNS, data))
    return token


def verify_token(token, first_name, last_name, email, expiration_date):
    expected_token = generate_token(first_name, last_name, email, expiration_date)
    return token == expected_token


def format_date(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d.%m.%Y")


def print_header():
    print("=== Token Authentication ===")


def print_token(token):
    print("Wygenerowany token:", token)


def print_access_granted():
    print("Token jest ważny. Dostęp przyznany.")


def print_access_denied():
    print("Token jest nieprawidłowy. Dostęp zabroniony.")


def input_user_data():
    first_name = input("Podaj imię: ")
    last_name = input("Podaj nazwisko: ")
    email = input("Podaj adres e-mail: ")
    expiration_date = input("Podaj datę ważności tokena (RRRR-MM-DD): ")
    return first_name, last_name, email, expiration_date


def input_token():
    return input("Podaj token do weryfikacji: ")


def print_user_data(user_data):
    print("Dane użytkownika:")
    print("Imię:", user_data['first_name'])
    print("Nazwisko:", user_data['last_name'])
    print("E-mail:", user_data['email'])
    print("Data ważności tokena:", format_date(user_data['expiration_date']))


def print_menu():
    print("Wybierz opcję:")
    print("1. Wygeneruj token")
    print("0. Wyjdź")


def main():
    print_header()
    while True:
        print_menu()
        choice = input("Twój wybór: ")
        if choice == "1":
            first_name, last_name, email, expiration_date = input_user_data()
            token = generate_token(first_name, last_name, email, expiration_date)
            print_token(token)
        elif choice == "0":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
