def check_horizontal_win_conditions(board, player):
    """returns True if the given player has a horizontal winning triple and False otherwise."""
    # Your code starts here.
    for row in board:
        char_count = 0
        for char in row:
            if char == player:
                char_count += 1
        if char_count == len(row):
            return True
    return False
    # Your code ends here.


def check_vertical_win_conditions(board, player):
    """returns True if the given player has a vertical winning triple and False otherwise."""
    # Your code starts here.
    for col_index in range(len(board[0])):
        char_count = 0
        for row_index in range(len(board)):
            if board[row_index][col_index] == player:
                char_count += 1
        if char_count == len(board):
            return True
    return False
    # Your code ends here.


def check_diagonal_win_conditions(board, player):
    """returns True if the given player has a diagonal winning triple and False otherwise."""
    # Your code starts here.
    diagonals = [[[0, 0], [1, 1], [2, 2]], [[2, 0], [1, 1], [0, 2]]]
    for diagonal in diagonals:
        char_count = 0
        for coordinate in diagonal:
            if board[coordinate[0]][coordinate[1]] == player:
                char_count += 1
        if char_count == len(diagonal):
            return True
    return False
    # Your code ends here.


def update_board(board, player, x, y):
    """
    updates the given coordinates(0-based) of the board with player's token.
    if the given coordinate corresponds to a nonnempty square returns False without making any modifications.
    returns True otherwise
    """
    # Your code starts here.
    if board[x][y] != None:
        return False

    board[x][y] = player
    return True
    # Your code ends here.


def get_square_representation(square):
    """ returns the character representation of the square"""
    if square == None:
        return ' '
    else:
        return square


def print_board(board):
    """prints the state of the board"""
    print(f'{get_square_representation(board[0][0])} | {get_square_representation(board[0][1])} | {get_square_representation(board[0][2])}\n'
          '---------\n'
          f'{get_square_representation(board[1][0])} | {get_square_representation(board[1][1])} | {get_square_representation(board[1][2])}\n'
          '---------\n'
          f'{get_square_representation(board[2][0])} | {get_square_representation(board[2][1])} | {get_square_representation(board[2][2])}')


board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

player_x = 'X'
player_o = 'O'
move_counter = 0

# Your code starts here
winner = None
while move_counter < 9:
    print_board(board)
    current_player = player_x if move_counter % 2 == 0 else player_o
    move_counter += 1

    x_coord = int(input(f'Player {current_player}, enter the x coordinate: '))
    y_coord = int(input(f'Player {current_player}, enter the y coordinate: '))
    while not update_board(board, current_player, x_coord, y_coord):
        x_coord = int(
            input(f'Player {current_player}, enter the x coordinate: '))
        y_coord = int(
            input(f'Player {current_player}, enter the y coordinate: '))

    if check_horizontal_win_conditions(board, current_player) or check_vertical_win_conditions(board, current_player) or check_diagonal_win_conditions(board, current_player):
        winner = current_player
        break

print_board(board)

if winner != None:
    print(
        f'Congratulations Player {winner}, you won the game in {move_counter} moves!')
else:
    print('Game resulted in a draw.')
# Your code ends here.
