tic_tac_toe_list = [
    ["[]", "[]", "[]"],
    ["[]", "[]", "[]"],
    ["[]", "[]", "[]"]
]

logo = """
 ______                ______                     ______                  
/\__  _\__            /\__  _\                   /\__  _\                 
\/_/\ \/\_\    ___    \/_/\ \/    __      ___    \/_/\ \/   ___      __   
   \ \ \/\ \  /'___\     \ \ \  /'__`\   /'___\     \ \ \  / __`\  /'__`\ 
    \ \ \ \ \/\ \__/      \ \ \/\ \L\.\_/\ \__/      \ \ \/\ \L\ \/\  __/ 
     \ \_\ \_\ \____\      \ \_\ \__/.\_\ \____\      \ \_\ \____/\ \____\\
      \/_/\/_/\/____/       \/_/\/__/\/_/\/____/       \/_/\/___/  \/____/
                                                                          
                                                                          """


def is_end_game():
    counter_row_x = [0, 0, 0]
    counter_row_o = [0, 0, 0]
    counter_column_x = [0, 0, 0]
    counter_column_o = [0, 0, 0]
    diagonal_x = 0
    diagonal_o = 0
    diagonal_other_x = 0
    diagonal_other_o = 0

    for i in range(3):
        for j in range(3):
            sym = tic_tac_toe_list[i][j]

            if sym == "x":
                counter_row_x[i] += 1
                counter_column_x[j] += 1

                if i == j:
                    diagonal_x += 1
                if i + j == 2:
                    diagonal_other_x += 1

            elif sym == "o":
                counter_row_o[i] += 1
                counter_column_o[j] += 1

                if i == j:
                    diagonal_o += 1
                if i + j == 2:
                    diagonal_other_o += 1

    for i in range(3):
        if counter_row_o[i] == 3 or counter_column_o[i] == 3 or diagonal_o == 3 or diagonal_other_o == 3:
            return "o"
        if counter_row_x[i] == 3 or counter_column_x[i] == 3 or diagonal_x == 3 or diagonal_other_x == 3:
            return "x"

    return None


def print_game():
    for i in range(3):
        for j in range(3):
            print(tic_tac_toe_list[i][j], end=" ")
        print("")


def player_move(i, j, symbol):
    tic_tac_toe_list[i][j] = symbol


def player_choose_square():
    flag = False
    while not flag:
        player_i = int(input("Give the row number! ")) - 1
        player_j = int(input("Give the column number! ")) - 1

        if player_i < 0 or player_i >= 3 or player_j < 0 or player_j >= 3:
            print("Choose a valid square!")
        elif tic_tac_toe_list[player_i][player_j] != "[]":
            print("Choose a free square!")
        else:
            flag = True

    return player_i, player_j


def game():
    print(f"Welcome to the\n {logo}")
    win = False
    i_player = 1
    while not win:

        symbol = ""
        if i_player % 2 == 0:
            print("Player O, go on!")
            symbol = "o"
        else:
            print("Player X, go on!")
            symbol = "x"

        print_game()
        player_move_i, player_move_j = player_choose_square()
        player_move(player_move_i, player_move_j, symbol)

        tmp = is_end_game()
        if tmp == "x":
            win = True
            print("Player X won!")
        elif tmp == "o":
            win = True
            print("Player O won!")

        i_player += 1
    print_game()


def main():
    game()


if __name__ == "__main__":
    main()
