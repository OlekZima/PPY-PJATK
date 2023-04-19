import math

number_list = []

for i in range(20):
    number_list.append(int(input("podaj liczbę w zakresie [-20; 20]")))

list_copy = number_list.copy()

list_prime_numbers = []

for num in number_list:
    if num > 1:
        flag = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            list_prime_numbers.append(num)

tuple_prime_numbers = tuple(list_prime_numbers)

print(tuple_prime_numbers)

list_squared_numbers = []

for num in number_list:
    if num % 2 == 0:
        list_squared_numbers.append(num ** 2)

tuple_squared = (list_squared_numbers)

print(tuple_squared)

for i in range(len(number_list)):
    if number_list[i] % 2 == 0:
        number_list[i] = 'A'

print(number_list)
