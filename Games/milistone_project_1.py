def print_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def user_pick_symbol_to_play():
    choice = 'wrong'
    while choice != 'X' and choice != 'O':
        choice = input("Please enter symbol to play (O or X): ")

    player_one = choice
    if player_one == 'X':
        player_two = 'O'
    else:
        player_two = 'X'

    return player_one, player_two


def player_choose_position(board, move):
    choice = 'wrong'
    within_range = False
    if move:
        print("Player 1 move!")
    else:
        print("Player 2 move!")

    while not choice.isdigit() or not within_range:
        choice = input("Please enter a number(1-9): ")

        if not choice.isdigit():
            print("Sorry that is not a digit")

        if choice.isdigit():
            if int(choice) in range(1, 10):
                if board[int(choice)] == ' ':
                    within_range = True
                else:
                    print("Already filled position, choose another position")
            else:
                print("Not in range")

    return int(choice)


def fill_board(board, symbol_to_fill, position_index):
    board[position_index] = symbol_to_fill
    return board


def check_horizontal(board, symbol_to_check):
    return (board[1] == board[2] == board[3] == symbol_to_check) or (
            board[4] == board[5] == board[6] == symbol_to_check) or (
                   board[7] == board[8] == board[9] == symbol_to_check)


def check_verticals(board, symbol_to_check):
    return (board[1] == board[4] == board[7] == symbol_to_check) or (
            board[2] == board[5] == board[8] == symbol_to_check) or (
                   board[3] == board[6] == board[9] == symbol_to_check)


def check_diagonals(board, symbol_to_check):
    return (board[1] == board[5] == board[9] == symbol_to_check) or (
            board[3] == board[5] == board[7] == symbol_to_check)


def check_for_the_win(board, symbol_to_check):
    return check_horizontal(board, symbol_to_check) or check_verticals(board, symbol_to_check) or check_diagonals(board, symbol_to_check)


def single_game():
    # initial board state
    board_state = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player_symbols = user_pick_symbol_to_play()
    someone_win = False
    # move == True if player 1 is playing now, False otherwise
    move = True
    print_board(board_state)
    while not someone_win:
        position_index = player_choose_position(board_state, move)
        if move:
            symbol_to_fill = player_symbols[0]
        else:
            symbol_to_fill = player_symbols[1]

        board_state = fill_board(board_state, symbol_to_fill, position_index)
        if ' ' not in board_state:
            print("No one win. You can try again :)")
            break

        someone_win = check_for_the_win(board_state, symbol_to_fill)
        print_board(board_state)
        if someone_win:
            if move:
                print("Player 1 win!!!")
            else:
                print("Player 2 win!!!")

        move = not move


def play_game():

    single_game()
    choice_to_play_again = 'wrong'

    while True:
        while choice_to_play_again != 'Y' and choice_to_play_again != 'N':
            choice_to_play_again = input("Do you want to play again(Y or N): ")

        if choice_to_play_again == 'Y':
            single_game()
            choice_to_play_again = 'wrong'
        else:
            print("Okiii, bye")
            break


play_game()
