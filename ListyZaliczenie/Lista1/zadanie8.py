def divisible_numbers(start, end, k_values):
    result = {}
    for k in k_values:
        result[k] = [i for i in range(start, end + 1) if i % k == 0]
    return result


start = int(input("Podaj początek przedziału: "))
end = int(input("Podaj koniec przedziału: "))
k_values = list(map(int, input("Podaj liczby k, oddzielone przecinkami: ").split(",")))
numbers_dict = divisible_numbers(start, end, k_values)
print(numbers_dict)
