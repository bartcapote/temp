import copy
import time
import os
import random


def init_boards(height):
    board1 = []
    for i in range(height):
        board1.append(['\033[36m~\033[0m'] * height)
    board2 = copy.deepcopy(board1)
    return board1, board2


def hide_ship_names(board):
    board = copy.deepcopy(board)
    for row in board:
        for index in range(len(row)):
            if row[index].isnumeric():
                row[index] = '\033[1mX\033[0m'
    return board


def print_board_with_hidden_ships(board):
    board_to_show = copy.deepcopy(board)
    for row in board_to_show:
        for index in range(len(row)):
            if row[index].isnumeric():
                row[index] = '\033[36m~\033[0m'
    print_board(board_to_show)


def print_board(board):
    board = hide_ship_names(board)
    os.system('clear')
    row_headers = "ABCDE"
    col_headers = "12345"
    for row in range(6):
        if row == 0:
            print("   " + " ".join(col_headers))
        else:
            print(row_headers[row - 1] + "  " + " ".join(board[row - 1]))


def toggle_player(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player


def get_input():
    user_input = input("Choose coordinates: ")
    return user_input


def wrong_input_message(board):
    print('\033[1m\033[31mWrong input! Try again.\033[0m')
    time.sleep(0.5)
    print_board(board)


def wrong_input_message_for_fire(board, player):
    print('\033[1m\033[31mWrong input! Try again.\033[0m')
    time.sleep(0.5)
    print_board_with_hidden_ships(board)
    print(f'Player {toggle_player(player)}: Fire!\n')


def convert_to_coordinates(user_input):
    alphabet_reference = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    row_index = alphabet_reference.find(user_input[0].upper())
    col_index = int(user_input[1]) - 1
    if len(user_input) > 2:
        direction = user_input[2]
        return row_index, col_index, direction
    return row_index, col_index


def check_input_format_big_ship(board, user_input):
    if (len(user_input) == 3 and user_input[0].isalpha()
       and user_input[1].isnumeric()
       and (user_input[2] == '|' or user_input[2] == '-')):
        return True
    else:
        wrong_input_message(board)
        return False


def check_input_format_small_ship(board, user_input):
    if len(user_input) == 2 and user_input[0].isalpha() and user_input[1].isnumeric():
        return True
    else:
        wrong_input_message(board)
        return False


def check_input_format_for_fire(board, user_input, player):
    if len(user_input) == 2 and user_input[0].isalpha() and user_input[1].isnumeric():
        return True
    else:
        wrong_input_message_for_fire(board, player)
        return False


def coordinates_in_board_for_big_ship(board, row_index, col_index, direction):
    board_height = len(board)
    if direction == '|':
        if row_index < board_height - 1 and col_index < board_height:
            return True
        else:
            wrong_input_message(board)
            return False
    if direction == '-':
        if row_index < board_height and col_index < board_height - 1:
            return True
        else:
            wrong_input_message(board)
            return False


def coordinates_in_board_for_small_ship(board, row_index, col_index):
    board_height = len(board)
    if row_index < board_height and col_index < board_height:
        return True
    else:
        wrong_input_message(board)
        return False


def coordinates_in_board_for_fire(board, row_index, col_index, player):
    board_height = len(board)
    if row_index < board_height and col_index < board_height:
        return True
    else:
        print('\033[1m\033[31mWrong input! Try again.\033[0m')
        time.sleep(0.5)
        os.system('clear')
        print_board_with_hidden_ships(board)
        print(f'\nPlayer {toggle_player(player)}: Fire!\n')
        return False


def move_not_touching_ships(board, row_index, col_index):
    index_range = len(board) - 1
    zero_case = False
    if board[row_index][col_index].isnumeric():
        return False
    if row_index == 0:
        row_index += 1
        zero_case = True
    if row_index - 1 <= index_range:
        if board[row_index - 1][col_index].isnumeric():
            return False
    if zero_case:
        row_index -= 1
        zero_case = False
    if row_index + 1 <= index_range:
        if board[row_index + 1][col_index].isnumeric():
            return False
    if col_index == 0:
        col_index += 1
        zero_case = True
    if col_index - 1 <= index_range:
        if board[row_index][col_index - 1].isnumeric():
            return False
    if zero_case:
        col_index -= 1
    if col_index + 1 <= index_range:
        if board[row_index][col_index + 1].isnumeric():
            return False
    return True


def more_ships_to_place(board, max_ships):
    ship_counter = 0
    for row in board:
        for cell in row:
            if cell.isnumeric():
                ship_counter += 1
    return True if ship_counter < max_ships else False


def place_small_ship(board, row_index, col_index, ship_name):
    board[row_index][col_index] = str(ship_name)
    return board


def place_big_ship(board, row_index, col_index, direction, ship_name):
    ship_name = str(ship_name)
    if direction == '-':
        board[row_index][col_index] = ship_name
        board[row_index][col_index + 1] = ship_name
    if direction == '|':
        board[row_index][col_index] = ship_name
        board[row_index + 1][col_index] = ship_name


def is_missed(board, row_index, col_index):
    if board[row_index][col_index].isnumeric():
        return False
    elif board[row_index][col_index] == '\033[31m\033[1mH\033[0m':
        print_board_with_hidden_ships(board)
        print('\033[1m\033[91mYou can\'t make more holes in there!\033[0m')
        time.sleep(.8)
        return False
    else:
        board[row_index][col_index] = "M"
        return True


def print_missed_message(board, row_index, col_index):
    if board[row_index][col_index] == "M":
        print("You've missed!")
        time.sleep(.5)


def is_hit(board, row_index, col_index):
    if board[row_index][col_index].isnumeric():
        board[row_index][col_index] = "\033[31m\033[1mH\033[0m"
        return True
    else:
        return False


def print_hit_message(board, row_index, col_index):
    if board[row_index][col_index] == "\033[31m\033[1mH\033[0m":
        print("You've hit the ship!")


def print_sunk_message():
    print('\033[1m\033[95mThey\'re sinking!\033[0m')


def is_sunk(board, row_index, col_index):
    pass  # sprawdza zawartość komórki, wyszukuje czy ta wartość jest jeszcze gdziekolwiek w tablicy
          # jeśli nie, to return True, wywołuje print_sunk()


def no_ships_left(board):
    pass   # sprawdza czy w boardzie gracza jest jakakolwiek komórka zawierająca wartość numeryczną
           # jeśli tak, to return True


def enemy_has_ships(player, board1, board2):
    player = toggle_player(player)
    if player == 1:
        board = board1
    else:
        board = board2
    for row in board:
        for cell in row:
            if cell.isnumeric():
                return True
            else:
                return False


def battleship_game():
    board1 = init_boards()[0]
    board2 = init_boards()[1]
    ship_name = 0
    player = 1
    # PLACEMENT PHASE:
    for i in range(2):
        if player == 1:
            board = board1
        else:
            board = board2
        # BIG SHIP:
        max_ships = 4
        while more_ships_to_place(board, max_ships):
            print_board(board)
            user_input = get_input()
            if check_input_format_big_ship(board, user_input):
                move_coordinates = convert_to_coordinates(user_input)
                row_index = move_coordinates[0]
                col_index = move_coordinates[1]
                direction = user_input[2]
                if (coordinates_in_board_for_big_ship(board, row_index, col_index, direction)
                   and move_not_touching_ships(board, row_index, col_index)):
                    if direction == '-':
                        if move_not_touching_ships(board, row_index, col_index + 1):
                            ship_name += 1
                            place_big_ship(board, row_index, col_index, direction, ship_name)
                        else:
                            wrong_input_message(board)
                    elif direction == '|':
                        if move_not_touching_ships(board, row_index + 1, col_index):
                            ship_name += 1
                            place_big_ship(board, row_index, col_index, direction, ship_name)
                        else:
                            wrong_input_message(board)
                else:
                    wrong_input_message(board)
                print_board(board)
        # SMALL SHIP:
        max_ships = 7
        while more_ships_to_place(board, max_ships):
            user_input = get_input()
            if check_input_format_small_ship(board, user_input):
                move_coordinates = convert_to_coordinates(user_input)
                row_index = move_coordinates[0]
                col_index = move_coordinates[1]
                if (coordinates_in_board_for_small_ship(board, row_index, col_index)
                   and move_not_touching_ships(board, row_index, col_index)):
                    ship_name += 1
                    place_small_ship(board, row_index, col_index, ship_name)
                    print_board(board)
                else:
                    wrong_input_message(board)
        print_board(board)
        toggle_player(player)
    #  FIRING PHASE:
    while enemy_has_ships(player, board1, board2):
        print_board(board2)
        user_input = get_input()
        if check_input_format_big_ship:
            move_coordinates = convert_to_coordinates(user_input)
            row_index = move_coordinates[0]
            col_index = move_coordinates[1]
            is_missed(board, row_index, col_index)
            is_hit(board, row_index, col_index)
            is_sunk(board, row_index, col_index)
        toggle_player(player)
    toggle_player(player)
    print(f'Player {player}, you sunk all the enemy ships! Good job, Admiral!')


if __name__ == "__main__":
    battleship_game()
