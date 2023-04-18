def exp_sum(x, N):
    sum = 0
    term = 1
    for i in range(N):
        sum += term
        term *= x / (i + 1)
    return sum


x = float(input("Podaj x: "))
N = int(input("Podaj N: "))
print(f"Suma wynosi {exp_sum(x, N)}")

