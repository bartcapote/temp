import copy
import time
import os
import random
import tkinter as tk


def init_boards():
    board1 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    board2 = copy.deepcopy(board1)
    return board1, board2


def print_board(board):
    row_headers = "ABCDE"
    col_headers = " 12345"
    for row in range(6):
        if row == 0:
            print(" " + "".join(col_headers))
        else:
            print(row_headers[row - 1] + " " + "".join(board[row - 1]))


def toggle_player(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player


def get_input():	
    col = input("col (A to E):")
    while col not in "ABCDE":
        print("That column is wrong! It should be A, B, C, D or E")
        col = input("column (A to E):")

    row = input("row (1 to 5):")
    while row not in "12345":
        print("That row is wrong! it should be 1, 2, 3, 4 or 5")
        row = input("row (1 to 5):")

    return row, col


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


def check_placement(board, input):	
    # ships are to close
    # if correct mark input
	return True	


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


def print_player_move_message(player):	

	print()	


def print_hit_message():
    msg1 = "Hit confirmed!"
    msg2 = "Citadel hit!"
    msg3 = "Boiler hit!"
    msg4 = "Smokestack hit!"
    msg5 = "Ammo rack hit!"
    hit_messages = {1: msg1, 2: msg2, 3: msg3, 4: msg4, 5: msg5}
    print(hit_messages[random.randrange(1, 5)])


def print_miss_message():	
    if row_index != 0 and col_index != 0:
        print("You've missed!")	


def print_sunk_message():
    if row_index == "X" and col_index == "X":
        print('Ship sunk!')


def display_waiting_screen():	
    sleep(2) 
    root.destroy()

    root = tk.Tk()
    root.title("Battleship")

    label = tk.Label(root, text="Wait for input.")
    label.pack()

    root.after(200, task)
    root.mainloop()

    print("You can start a game now.")


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


if __name__ == "__main__":
    battleship_game()
