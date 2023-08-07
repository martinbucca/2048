import random
import gamelib as gamelib
from constants import *


class Game:
    def __init__(self):
        ''' 
        Initializes the game board with a all the cells empty and a random cell with a value from the possible initial values.
        '''
        self.board = [[EMPTY for j in range(COLUMNS)] for i in range(ROWS)]
        self.insert_random_new_cell()
        self.score = INITIAL_SCORE
    def show(self):
        ''' 
        Shows the game board on the screen.
        '''
        gamelib.draw_rectangle(0, 0, 800, 600, fill=BACKGROUND_COLOR)
        gamelib.draw_text("Score", SCORE_LABEL_POSITION[0], SCORE_LABEL_POSITION[1], size=30, fill="white")
        gamelib.draw_text(str(self.score), SCORE_POSITION[0], SCORE_POSITION[1], size=30, fill="white")
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                x1, y1 = BOARD_X_MARGIN + j * CELL_SIZE + 2 * j, BOARD_Y_MARGIN + i * CELL_SIZE + 2 * i
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                value = self.board[i][j]
                gamelib.draw_rectangle(x1, y1, x2, y2, fill=COLORS.get(value, DEFAULT_CELL_COLOR), outline=COLORS.get(value, DEFAULT_CELL_COLOR))
                if value != EMPTY:
                    gamelib.draw_text(str(value), (x1 + x2) / 2, (y1 + y2) / 2, fill=NUMBERS_COLOR)
    def get_random_empty_cell(self):
        '''
        Returns a random empty cell from the board. If there are no empty cells, returns False.
        '''
        empty_cells = [(i, j) for i in range(ROWS) for j in range(COLUMNS) if self.board[i][j] == EMPTY]
        return random.choice(empty_cells) if empty_cells else False
    def insert_random_new_cell(self):
        '''
        Inserts a new cell with a value from the possible initial values in a random empty cell of the board.
        '''
        row, column = (self.get_random_empty_cell())
        self.board[row][column] = random.choice(POSSIBLE_INITIAL_VALUES)
    def move_left(self):
        '''
        Moves the board to the left, combining the numbers that can be combined and moving them to the left.
        '''
        changed = False
        for row in range(ROWS):
            if self.combine_row(row):
                changed = True
        return changed
    def combine_row(self, row_index):
        '''
        Combines the numbers of a line that can be combined and moves them to the left.
        If there are no combinable numbers, returns the original line.
        '''
        row = self.board[row_index]
        combinable_numbers = [number for number in row if number != EMPTY]
        if combinable_numbers:
            result = []
            i = 0
            while i < len(combinable_numbers):
                if i < len(combinable_numbers) - 1 and combinable_numbers[i] == combinable_numbers[i + 1]:
                    result.append(combinable_numbers[i] * 2)
                    self.score += combinable_numbers[i] * 2
                    i += 2
                else:
                    result.append(combinable_numbers[i])
                    i += 1
            empty_cells_to_add = len(row) - len(result)
            result += [EMPTY] * empty_cells_to_add
            self.board[row_index] = result
            return result != row
        return False
    def move_right(self):
        '''
        Moves the board to the right, combining the numbers that can be combined and moving them to the right.
        '''
        self.invert_board()
        changed = self.move_left()
        self.invert_board()
        return changed
    def invert_board(self):
        '''
        Inverts the rows of the board.
        '''
        self.board = [list(reversed(row)) for row in self.board]
    def transpose_board(self):
        '''
        Transposes the rows and columns of the board.
        '''
        self.board = [[row[i] for row in self.board] for i in range(COLUMNS)]
    def move_up(self):
        '''
        Moves the board to the up, combining the numbers that can be combined and moving them to the up.
        '''
        self.transpose_board()
        changed = self.move_left()
        self.transpose_board()
        return changed
    def move_down(self):
        '''
        Moves the board to the down, combining the numbers that can be combined and moving them to the down.
        '''
        self.transpose_board()
        changed = self.move_right()
        self.transpose_board()
        return changed
    def update(self, direction):
        '''Updates the game according to the specified movement in the desired direction to move the board.'''
        changed = False
        if direction == UP:
            changed = self.move_up()
        elif direction == DOWN:
            changed = self.move_down()
        elif direction == LEFT:
            changed = self.move_left()
        elif direction == RIGHT:
            changed = self.move_right()
        if changed:
            self.insert_random_new_cell()
    def won(self):
        '''
        Returns True if the game is won, False otherwise.
        '''
        for i in range(ROWS):
            if WIN_NUMBER in self.board[i]:
                return True
        return False
    def lost(self):
        '''
        Returns True if the game is lost, False otherwise.
        '''
        if not self.possible_horizontal_moves() and not self.possible_vertical_moves():
            return True
        return False
    def possible_vertical_moves(self):
        '''
        Returns True if there are vertical moves possible, False otherwise.
        '''
        result =  self.possible_horizontal_moves(self.transpose_board())
        self.transpose_board()
        return result
    def possible_horizontal_moves(self):
        '''
        Returns True if there are horizontal moves possible, False otherwise.
        '''
        for i in range(ROWS):
            if self.possible_moves_in_row(self.board[i]):
                return True
        return False
    def possible_moves_in_row(self, row):
        '''
        Returns True if there are possible moves in the row, False otherwise.
        '''
        i = 0
        while i < len(row):
            if row[i] == EMPTY:
                return True
            if i < len(row) - 1 and row[i] == row[i + 1]:
                return True
            i += 1
        return False
    





















