nicki = ["Hiroshima Yamamoto", "Park Kyung-Mo", "Lee Sung Jin", "Michele Frangilli", "Marco Galiazzo", "Darrell Pace", "Ki Bo Bae", "Yun Mi-Jin", "Im Hyun", "Kim Soo Nyung"]
punkty_przed = [275, 262, 256, 249, 246, 245, 243, 242, 239, 238]
punkty_po = [295, 292, 286, 279, 276, 275, 273, 272, 269, 268]
daty = ['2022-03-01', '2022-03-02', '2022-03-03', '2022-03-04', '2022-03-05', '2022-03-06', '2022-03-07', '2022-03-08', '2022-03-09', '2022-03-10']

wyniki = {nick: [{"data": daty[i], "punkty": punkty_przed[i]} for i in range(len(daty))] for nick in nicki}

for i, nick in enumerate(nicki):
    for j in range(len(daty)):
        if wyniki[nick][j]["data"] >= "2022-03-05":
            wyniki[nick][j]["punkty"] = punkty_po[i]

print(wyniki)
