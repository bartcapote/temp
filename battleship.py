import copy
import time
import os


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
