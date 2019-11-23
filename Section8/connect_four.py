"""
Koc University, Turkey
KOLT Python Certificate Program
Spring 2019 - Assignment 1
Created by @ahmetuysal
"""


def print_board(board):
    for row in board[::-1]:
        print(' '.join(row))


def play_the_move(board, column_no, player_piece):
    for index, row in enumerate(board):
        if row[column_no] == '*':
            row[column_no] = player_piece
            return index


def has_horizontal_win_condition(board, row_no, column_no, player_piece):
    match_count = 0
    for piece in board[row_no][max(0, column_no-3):column_no+4]:
        if piece == player_piece:
            match_count += 1
        else:
            match_count = 0

        if match_count == 4:
            return True
    return False


def has_vertical_win_condition(board, row_no, column_no, player_piece):
    match_count = 0
    for row in board[max(0, row_no-3):row_no+4]:
        piece = row[column_no]
        if piece == player_piece:
            match_count += 1
        else:
            match_count = 0

        if match_count == 4:
            return True
    return False


def has_main_diagonal_win_condition(board, row_no, column_no, player_piece):
    match_count = 0
    for i in range(-3, 4):
        row_index = row_no + i
        column_index = column_no + i
        # if piece we are checking is out of bounds
        if row_index not in range(len(board)) or column_index not in range((len(board[0]))):
            match_count = 0
            continue

        piece = board[row_index][column_index]
        if piece == player_piece:
            match_count += 1
        else:
            match_count = 0

        if match_count == 4:
            return True
    return False


def has_antidiagonal_win_condition(board, row_no, column_no, player_piece):
    match_count = 0
    for i in range(-3, 4):
        row_index = row_no + i
        column_index = column_no - i
        # if piece we are checking is out of bounds
        if row_index not in range(len(board)) or column_index not in range((len(board[0]))):
            match_count = 0
            continue

        piece = board[row_index][column_index]
        if piece == player_piece:
            match_count += 1
        else:
            match_count = 0

        if match_count == 4:
            return True
    return False


def has_win_condition(board, row_no, column_no, player_piece):
    return (has_horizontal_win_condition(board, row_no, column_no,
                                         player_piece)
            or has_vertical_win_condition(board, row_no, column_no,
                                          player_piece)
            or has_main_diagonal_win_condition(board, row_no, column_no,
                                               player_piece)
            or has_antidiagonal_win_condition(board, row_no, column_no,
                                              player_piece))


print('Welcome to two player Connect Four game!')
print('This a two player game played on a seven-column, six-row board.')

# empty squares are denoted with *
board = (
    ['*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*'])

players = []
player_pieces = []

# Take player names
players.append(input('Enter your name player 1: '))
players.append(input('Enter your name player 2: '))

# Take player piece symbols
# Symbols need be unique and have length 1
# They should also be different than '*'
print('\'*\' symbol is reserved to denote empty squares.')


for player_name in players:
    player_piece = input(f'{player_name} please pick a symbol: ')

    while len(player_piece) != 1 or player_piece == '*' or player_piece in player_pieces:
        player_piece = input(f'{player_name} please pick a symbol: ')

    player_pieces.append(player_piece)


# Print the initial board
print_board(board)

# Loop for game
for move_counter in range(42):
    # Take user input for column_no
    player_name = players[move_counter % len(players)]
    player_piece = player_pieces[move_counter % len(player_pieces)]
    column_no = input(f'{player_name} please enter column number: ')
    # Check whether this is a valid move
    # It needs to be an integer, hint: use str.isnumeric()
    # It needs to be in range [0, 6] inclusive
    # And the selected column cannot be full
    # You need to ask for new column_no until user enters a valid one
    while not column_no.isnumeric() or int(column_no) not in range(0, 7) or board[-1][int(column_no)] != '*':
        column_no = input(f'{player_name} please enter column number: ')
    # Play the move
    column_no = int(column_no)
    row_no = play_the_move(board, column_no, player_piece)
    # Print the current board
    print_board(board)
    # Check whether the game is finished

    # Print the winner and number of moves if game is finished
    # The game should stop at this point if game is finished
    if has_win_condition(board, row_no, column_no, player_piece):
        print(
            f'Congratulations {player_name} you won the game in {move_counter + 1} moves.')
        break
# this else block only runs if condition on while loop becomes false
# it is not executed if loop is terminated by a break statement
# i.e when all 42 moves are played without a break statement
else:
    print('There are no other legal moves, the game ended in a draw.')
