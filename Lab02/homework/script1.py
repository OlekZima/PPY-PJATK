slowo_jeden = input("Podaj pierwsze słowo: ")
slowo_dwa = input("Podaj drugie słowo: ")

slowo_jeden = slowo_jeden.replace("a", "7")
slowo_jeden = slowo_jeden.replace("ą", "7")
slowo_jeden = slowo_jeden.replace("e", "7")
slowo_jeden = slowo_jeden.replace("ę", "7")
slowo_jeden = slowo_jeden.replace("o", "7")
slowo_jeden = slowo_jeden.replace("ó", "7")
slowo_jeden = slowo_jeden.replace("i", "7")
slowo_jeden = slowo_jeden.replace("y", "7")
slowo_jeden = slowo_jeden.replace("u", "7")

slowo_dwa = slowo_dwa.replace("w", "6")
slowo_dwa = slowo_dwa.replace("r", "6")
slowo_dwa = slowo_dwa.replace("t", "6")
slowo_dwa = slowo_dwa.replace("p", "6")
slowo_dwa = slowo_dwa.replace("s", "6")
slowo_dwa = slowo_dwa.replace("d", "6")
slowo_dwa = slowo_dwa.replace("f", "6")
slowo_dwa = slowo_dwa.replace("g", "6")
slowo_dwa = slowo_dwa.replace("h", "6")
slowo_dwa = slowo_dwa.replace("k", "6")
slowo_dwa = slowo_dwa.replace("l", "6")
slowo_dwa = slowo_dwa.replace("z", "6")
slowo_dwa = slowo_dwa.replace("x", "6")
slowo_dwa = slowo_dwa.replace("c", "6")
slowo_dwa = slowo_dwa.replace("b", "6")
slowo_dwa = slowo_dwa.replace("n", "6")
slowo_dwa = slowo_dwa.replace("m", "6")
slowo_dwa = slowo_dwa.replace("ż", "6")
slowo_dwa = slowo_dwa.replace("ź", "6")
slowo_dwa = slowo_dwa.replace("ś", "6")
slowo_dwa = slowo_dwa.replace("ł", "6")
slowo_dwa = slowo_dwa.replace("ć", "6")
slowo_dwa = slowo_dwa.replace("ń", "6")
slowo_dwa = slowo_dwa.replace("j", "6")

slowo_suma = (slowo_jeden + slowo_dwa).upper()
print(slowo_suma)
