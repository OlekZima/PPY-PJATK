"""
Lab02 - typ Boolean, operatory arytmetyczne
"""

a = True
b = False

print(a, b)

# operatory wyrażeń Boolean
x = 2
y = 4

print()

print(x < y)
print(x > y)
print(x <= y)
print(x >= y)
print(x == y)
print(x != y)

print()

print(a or b)
print(a and b)
print(not a)
print(not b)

print()

# operatory arytmetyczne
a, b = 2, 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# Zmiana wartości zmiennych
a, b, c, d, e = 1, 3, 7, 4, 6
a += 2
b -= 2
c *= 2
d /= 2

print(a, b, c, d, e)
