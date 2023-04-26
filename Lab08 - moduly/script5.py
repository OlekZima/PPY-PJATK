"""
Lab08 - moduł 'random'
"""

import random

#       DANGER
#   nazwy funkcji dostępne bez użycia nazwy modułu
# from random import *
#       DANGER

# from random import randint

random.seed()
print(random.randint(1, 15))
print(random.randint(1, 15))

lista_range = list(range(1, 10))
print(random.choice(lista_range))

random.shuffle(lista_range)
print(lista_range)

print(random.random())

print(random.uniform(10, 30))
