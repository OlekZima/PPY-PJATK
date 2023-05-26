def main():
    stars = int(input("Podaj liczbę gwizdek: "))
    hashes = int(input("Podaj liczbę kratek: "))
    dollars = int(input("Podaj liczbę dollarów: "))

    max_iterations = max(stars, hashes, dollars)

    for i in range(max_iterations):
        if stars <= 0:
            print(" \t", end="")
        else:
            print("*\t", end="")
        stars -= 1

        if hashes <= 0:
            print(" \t", end="")
        else:
            print("#\t", end="")
        hashes -= 1

        # with endline, because $ is the last char in the row. Without \t for the same reason
        if dollars <= 0:
            print(" ")
        else:
            print("$")
        dollars -= 1


if __name__ == "__main__":
    main()
