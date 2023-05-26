from math import sqrt


def main():
    num1 = int(input("Podaj pierwszą liczbę: "))
    num2 = int(input("Podaj pierwszą liczbę: "))

    operation = input("Podaj działanie, +, -, *, /, %, sqrt, anyroot, ^: ")

    if operation == "+":
        print(f"Wynikiem działania {num1} {operation} {num2} jest {num1 + num2}")
    elif operation == "-":
        print(f"Wynikiem działania {num1} {operation} {num2} jest {num1 - num2}")
    elif operation == "*":
        print(f"Wynikiem działania {num1} {operation} {num2} jest {num1 * num2}")
    elif operation == "/":
        print(f"Wynikiem działania {num1} {operation} {num2} jest {num1 / num2}")
    elif operation == "%":
        print(f"Wynikiem działania {num1} {operation} {num2} jest {num1 % num2}")
    elif operation == "sqrt":
        print(f"Wynikiem działania {operation}({num1}) jest {num1 ** (1/2)}")
        print(f"Wynikiem działania {operation}({num2}) jest {num2 ** (1/2)}")
    elif operation == "anyroot":
        print(f"Wynikiem działania {num1}_root({num2}) jest {num2 ** (1 / num1)}")
    elif operation == "^":
        print(f"Wynikiem działania {num1} {operation} {num2} jest {num1 ** num2}")


if __name__ == "__main__":
    main()
