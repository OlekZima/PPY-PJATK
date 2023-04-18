def divisible_by_k(start, end, k, output_type="list"):
    result = []
    for i in range(start, end + 1):
        if i % k == 0:
            if output_type == "list":
                result.append(i)
            elif output_type == "dict":
                result.append({"number": i, "divisible_by": k})
    return result


k = int(input("Podaj liczbe k: "))

output_type = input("Wybierz rodzaj wyjscia (list/dict): ")

if output_type == "list":
    print(divisible_by_k(20, 80, k))
elif output_type == "dict":
    print(divisible_by_k(20, 80, k, "dict"))
