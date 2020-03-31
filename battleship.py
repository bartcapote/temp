import copy
import time
import os
import random


def init_boards():
    board1 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    board2 = copy.deepcopy(board1)
    return board1, board2


def toggle_player(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player


def wrong_input_message(board):
    print('\033[1m\033[31mWrong input! Try again.\033[0m')
    time.sleep(0.8)
    os.system('clear')
    # print_board(board)  -  COMMENT OUT UNTIL print_board() IS DEFINED


def check_input(board, user_input):
    alphabet_reference = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    if len(user_input) == 2 and user_input[0].isalpha() and user_input[1].isnumeric():
        row_index = alphabet_reference.find(user_input[0].upper())
        col_index = int(user_input[1]) - 1
        board_height = len(board)
        if row_index < board_height and col_index < board_height:
            return True
        else:
            wrong_input_message(board)
            return False
    else:
        wrong_input_message(board)
        return False


def check_ships_left(board, max_ships):
    ship_counter = 0
    for row in board:
        for cell in row:
            ship_counter += 1 if cell == 'X' else 0
    return True if ship_counter < max_ships else False


def place_ship(board, user_input):
    alphabet_reference = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    row_index = alphabet_reference.find(user_input[0].upper())
    col_index = int(user_input[1]) - 1
    board[row_index][col_index] = 'X'


def print_hit_message():
    msg1 = "Hit confirmed!"
    msg2 = "Citadel hit!"
    msg3 = "Boiler hit!"
    msg4 = "Smokestack hit!"
    msg5 = "Ammo rack hit!"
    hit_messages = {1: msg1, 2: msg2, 3: msg3, 4: msg4, 5: msg5}
    print(hit_messages[random.randrange(1, 5)])


def print_sunk_message():
    print('Ship sunk!')


def battleship_game():
    max_ships = 8
    board1 = init_boards()[0]
    while check_ships_left(board1, max_ships):
        # board2 = init_boards()[1]         |
        # print_board(board1)               |
        # user_input = get_input(board1)    |
        # place_ship(board1, user_input)    |
        # print_board(board1)               | COMMENT OUT UNTIL REFERENCES DEFINED
        pass
