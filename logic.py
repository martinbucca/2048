import random
import gamelib as gamelib
from constants import *






def initialize_2048():
    ''' 
    Initializes the game board with a all the cells empty and a random cell with a value from the possible initial values.
    '''
    initial_board = [[EMPTY for j in range(COLUMNS)] for i in range(ROWS)]
    initial_row, initial_column = get_random_empty_cell(initial_board)
    initial_board[initial_row][initial_column] = random.choice(POSSIBLE_INITIAL_VALUES)
    return initial_board


def show_ui(board):
    ''' 
    Shows the game board on the screen.
    '''
    for i in range(ROWS):
        for j in range(COLUMNS):
            x1, y1 = 200 + j * 100, 50 + i * 100
            x2, y2 = x1 + 100, y1 + 100
            value = board[i][j]
            gamelib.draw_rectangle(x1, y1, x2, y2, fill=COLORS.get(value, "#cdc1b4"))
            if value != EMPTY:
                gamelib.draw_text(str(value), (x1 + x2) / 2, (y1 + y2) / 2, fill="black")




def no_vertical_moves(board):
    return no_horizontal_moves(transpose_board(board))

def no_horizontal_moves(board):
    for i in range(ROWS):
        for j in range(1, COLUMNS):
            if board[i][j - 1] == board[i][j]:
                return False
    return True



def game_won(board):
    for i in range(ROWS):
        for j in range(COLUMNS):
            if board[i][j] == WIN_NUMBER:
                return True
    return False


def lost_game(board):
    occupied_cells = 0
    for i in range(ROWS):
        for j in range(COLUMNS):
            if board[i][j]:
                occupied_cells += 1
    if occupied_cells == ROWS * COLUMNS and no_horizontal_moves(board) and no_vertical_moves(board):
        return True
    return False
    

def invert_board(board):
    '''
    Inverts the rows of the board.
    '''
    return [list(reversed(row)) for row in board]

def transpose_board(board):
    '''
    Transposes the rows and columns of the board.
    '''
    transposed_board = [[row[i] for row in board] for i in range(COLUMNS)]
    return transposed_board

def combine_line(line):
    '''
    Combines the numbers of a line that can be combined and moves them to the left.
    If there are no combinable numbers, returns the original line.
    '''
    combinable_numbers = [number for number in line if number != EMPTY]
    if not combinable_numbers:
        return line
    result = []
    i = 0
    while i < len(combinable_numbers):
        if i < len(combinable_numbers) - 1 and combinable_numbers[i] == combinable_numbers[i + 1]:
            result.append(combinable_numbers[i] * 2)
            i += 2
        else:
            result.append(combinable_numbers[i])
            i += 1

    # Añadir ceros al final hasta completar el largo de la fila original
    empty_cells_to_add = len(line) - len(result)
    result += [EMPTY] * empty_cells_to_add
    return result

def move_left(board):
    '''
    Moves the board to the left, combining the numbers that can be combined and moving them to the left.
    '''
    moved_board = board.copy()
    for i in range(ROWS):
        moved_board[i] = combine_line(moved_board[i])
    return moved_board

def move_up(board):
    '''
    Moves the board to the up, combining the numbers that can be combined and moving them to the up.
    '''
    transposed_board = transpose_board(board)
    moved_board = move_left(transposed_board)
    return transpose_board(moved_board)

def move_down(board):
    '''
    Moves the board to the down, combining the numbers that can be combined and moving them to the down.
    '''
    transposed_board = transpose_board(board)
    moved_board = move_right(transposed_board)
    return transpose_board(moved_board)

def move_right(board):
    '''
    Moves the board to the right, combining the numbers that can be combined and moving them to the right.
    '''
    inverted_board = invert_board(board)
    moved_board = move_left(inverted_board)
    return invert_board(moved_board)

def update_game(board, direction):
    '''Updates the game according to the specified movement in the desired direction to move the board.'''
    if direction == UP:
        return move_up(board)
    elif direction == DOWN:
        return move_down(board)
    elif direction == LEFT:
        return move_left(board)
    elif direction == RIGHT:
        return move_right(board)

def get_random_empty_cell(board):
    '''
    Returns a random empty cell from the board. If there are no empty cells, returns False.
    '''
    empty_cells = [(i, j) for i in range(ROWS) for j in range(COLUMNS) if board[i][j] == EMPTY]
    return random.choice(empty_cells) if empty_cells else False

def insert_random_new_cell(board):
    '''
    Inserts a new cell with a value from the possible initial values in a random empty cell of the board.
    '''
    row, column = (get_random_empty_cell(board))
    board[row][column] = random.choice(POSSIBLE_INITIAL_VALUES)
    return board








