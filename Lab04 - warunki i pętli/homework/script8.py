flag = True

while flag:
    print("Z którego systemu chcesz konwertować?")
    print("1. Binary (2)")
    print("2. Octal (8)")
    print("3. Decimal (10)")
    print("4. Hex (16)")
    decide1 = int(input("Wybierz jedną opcję (wpisz liczbę): "))

    print("\nNa który system konwertujesz?")
    print("1. Binary (2)")
    print("2. Octal (8)")
    print("3. Decimal (10)")
    print("4. Hex (16)")
    decide2 = int(input("Wybierz jedną opcję (wpisz liczbę): "))

    if decide1 == decide2:
        print("\n\nNo weź...\n\n")
        continue

    if decide1 == 1:
        bin_number = int((input("Podaj liczbę w systemie dwójkowym: ")), 2)
        if decide2 == 2:
            print(
                f"\n\nTwoja liczba binarna {bin(bin_number)} w systemie oktalnym wygląda tak {format(bin_number, '#o')}\n\n")
        elif decide2 == 3:
            print(
                f"\n\nTwoja liczba binarna {bin(bin_number)} w systemie decymalnym wygląda tak {format(bin_number, '#d')}\n\n")
        elif decide2 == 4:
            print(
                f"\n\nTwoja liczba binarna {bin(bin_number)} w systemie hex wygląda tak {format(bin_number, '#X')}\n\n")
    elif decide1 == 2:
        octa_number = int(input("Podaj liczbę w systemie octalnym: "), 8)
        if decide2 == 1:
            print(
                f"\n\nTwoja liczba octalna {oct(octa_number)} w systemie binarnym wygląda tak {format(octa_number, '#b')}\n\n")
        elif decide2 == 3:
            print(
                f"\n\nTwoja liczba octalna {oct(octa_number)} w systemie decymalnym wygląda tak {format(octa_number, '#d')}\n\n")
        elif decide2 == 4:
            print(
                f"\n\nTwoja liczba octalna {oct(octa_number)} w systemie hex wygląda tak {format(octa_number, '#X')}\n\n")
    elif decide1 == 3:
        dec_num = int(input("Podaj liczbę w systemie decymalnym: "))
        if decide2 == 1:
            print(
                f"\n\nTwoja liczba decymalna {dec_num} w systemie bin wygląda tak {format(dec_num, '#b')}\n\n")
        elif decide2 == 2:
            print(
                f"\n\nTwoja liczba decymalna {dec_num} w systemie octal wygląda tak {format(dec_num, '#o')}\n\n")
        elif decide2 == 4:
            print(
                f"\n\nTwoja liczba decymalna {dec_num} w systemie hex wygląda tak {format(dec_num, '#X')}\n\n")
    elif decide1 == 4:
        hex_num = int(input("Podaj liczbę w systemie hex: "), 16)
        if decide2 == 1:
            print(f"\n\nTwoja liczba hex {hex(hex_num)} w systemie bin wygląda tak {format(hex_num, '#b')}\n\n")
        elif decide2 == 2:
            print(f"\n\nTwoja liczba hex {hex(hex_num)} w systemie octa wygląda tak {format(hex_num, '#o')}\n\n")
        elif decide2 == 3:
            print(f"\n\nTwoja liczba hex {hex(hex_num)} w systemie dec wygląda tak {format(hex_num, '#d')}\n\n")
