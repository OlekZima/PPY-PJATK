import math


def catalan_numbers(x):
    n = 0
    while True:
        catalan_num = int(math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n)))
        if catalan_num < x:
            print(catalan_num, end="\t")
            n += 1
        else:
            break


how_many_numbers = int(input("Podaj liczbę naturalną: "))
catalan_numbers(how_many_numbers)
