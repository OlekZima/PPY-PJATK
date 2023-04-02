import math


def catalan_numbers(x):
    n = 0
    while True:
        catalan_num = int(math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n)))
        if catalan_num < x:
            print(catalan_num, end="\t")
            n += 1
        else:
            return catalan_num


how_many_numbers = int(input("Podaj liczbę naturalną: "))
x = catalan_numbers(how_many_numbers)
