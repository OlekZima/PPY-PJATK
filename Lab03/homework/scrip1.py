name = input("Podaj imię: ")
birth_date = input("Podaj datę urodzin: ")
mail_adress = input("Podaj adres e-mail: ")
phone_numer = input("Podaj numer telefonu: ")

list = [name, birth_date, mail_adress, phone_numer]

tuple = (name, birth_date, mail_adress, phone_numer)

dictionary = {name, birth_date, mail_adress, phone_numer}

print(f"List: {list}")
print(f"tuple: {tuple}")
print(f"dictionary: {dictionary}")
