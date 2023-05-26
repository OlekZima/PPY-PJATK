tic_tac_toe_list = [
    ["[]", "[]", "o"],
    ["o", "x", "o"],
    ["x", "x", "o"]
]


def is_end_game():
    counter_column_x = 0
    counter_column_o = 0

    x = 0

    for i in range(3):

        if tic_tac_toe_list[i][x] == "x":
            counter_column_x += 1
        elif tic_tac_toe_list[i][x] == "o":
            counter_column_o += 1
        x += 1

        counter_row_x = 0
        counter_row_o = 0

        for j in range(3):
            if tic_tac_toe_list[i][j] == "x":
                counter_row_x += 1
            elif tic_tac_toe_list[i][j] == "o":
                counter_row_o += 1

        if counter_row_o == 3 or counter_row_x == 3:
            return 1

        if counter_row_x == 3 or counter_column_o == 3:
            return 0

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
        player_i = int(input("Give the row number!"))
        player_j = int(input("Give the column number!"))
        if tic_tac_toe_list[player_i][player_j] != "[]":
            print("Choose free square!")
        else:
            flag = True
    return player_i, player_j


def game():
    print("Welcome to the Tic Tac Toe in Python!")
    win = False
    i_player = 0
    while not win:
        print_game()
        symbol = ""
        if i_player % 2 == 0:
            symbol = "o"
        else:
            symbol = "x"
    player_move_i, player_move_j = player_choose_square()
    player_move(player_move_i, player_move_j, symbol)


print(is_end_game())
