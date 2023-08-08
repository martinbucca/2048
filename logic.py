"""
This module contains the logic of the game.
"""

import random
import gamelib
from constants import *


class Game:
    """
    This class represents the game. It contains the game board and the game score.
    """

    def __init__(self):
        """
        Initializes the game board with a all the cells empty and a random cell
        with a value from the possible initial values.
        """
        self.board = [[EMPTY for j in range(COLUMNS)] for i in range(ROWS)]
        self.generate_initial_cells()
        self.score = INITIAL_SCORE

    def generate_initial_cells(self):
        """
        Generates the initial cells of the game board.
        """
        self.insert_random_new_cell()
        self.insert_random_new_cell()

    def reset(self):
        """
        Resets the game board with a all the cells empty and a random cell
        with a value from the possible initial values.
        """
        self.board = [[EMPTY for j in range(COLUMNS)] for i in range(ROWS)]
        self.generate_initial_cells()
        self.score = INITIAL_SCORE

    def show(self):
        """
        Shows the game board on the screen.
        """
        # Background
        gamelib.draw_rectangle(
            0,
            0,
            WINDOW_SIZE[0],
            WINDOW_SIZE[1],
            fill=BACKGROUND_COLOR,
            outline=BACKGROUND_COLOR,
        )
        # Board background
        gamelib.draw_rectangle(
            BOARD_X_MARGIN - CELL_PADDING,
            BOARD_Y_MARGIN - CELL_PADDING,
            BOARD_X_MARGIN
            + CELL_SIZE * ROWS
            + CELL_PADDING * (ROWS - 1)
            + CELL_PADDING,
            BOARD_Y_MARGIN
            + CELL_SIZE * COLUMNS
            + CELL_PADDING * (COLUMNS - 1)
            + CELL_PADDING,
            fill=BOARD_BACKGROUND_COLOR,
            outline=BOARD_BACKGROUND_COLOR,
        )
        # New game button
        gamelib.draw_rectangle(
            NEW_GAME_BUTTON[0],
            NEW_GAME_BUTTON[1],
            NEW_GAME_BUTTON[2],
            NEW_GAME_BUTTON[3],
            fill=NEW_GAME_BUTTON_COLOR,
            activeoutline="black",
            activewidth=2,
            outline="black",
        )
        gamelib.draw_text(
            "New Game",
            (NEW_GAME_BUTTON[0] + NEW_GAME_BUTTON[2]) / 2,
            (NEW_GAME_BUTTON[1] + NEW_GAME_BUTTON[3]) / 2,
            size=14,
            fill="white",
            font="Helvetica",
        )
        # Score
        gamelib.draw_rectangle(
            BOARD_X_MARGIN - CELL_PADDING,
            50,
            BOARD_X_MARGIN + CELL_SIZE,
            105,
            fill="#8F7A66",
            outline="#8F7A66",
        )
        gamelib.draw_text(
            "SCORE",
            (BOARD_X_MARGIN - CELL_PADDING + BOARD_X_MARGIN + CELL_SIZE) / 2,
            65,
            size=14,
            fill="white",
            font="Helvetica",
        )
        gamelib.draw_text(
            str(self.score),
            (BOARD_X_MARGIN - CELL_PADDING + BOARD_X_MARGIN + CELL_SIZE) / 2,
            90,
            size=16,
            fill="white",
            font="Helvetica",
        )
        # Best
        gamelib.draw_rectangle(
            BOARD_X_MARGIN + CELL_SIZE + CELL_PADDING,
            50,
            BOARD_X_MARGIN + 2 * CELL_SIZE + CELL_PADDING,
            105,
            fill="#8F7A66",
            outline="#8F7A66",
        )
        gamelib.draw_text(
            "BEST",
            (
                BOARD_X_MARGIN
                + CELL_SIZE
                + CELL_PADDING
                + BOARD_X_MARGIN
                + 2 * CELL_SIZE
                + CELL_PADDING
            )
            / 2,
            65,
            size=14,
            fill="white",
            font="Helvetica",
        )
        gamelib.draw_text(
            str(self.score),
            (
                BOARD_X_MARGIN
                + CELL_SIZE
                + CELL_PADDING
                + BOARD_X_MARGIN
                + 2 * CELL_SIZE
                + CELL_PADDING
            )
            / 2,
            90,
            size=16,
            fill="white",
            font="Helvetica",
        )
        
        # gamelib.draw_text(
        #    str(self.score), SCORE_POSITION[0], SCORE_POSITION[1], size=30, fill="black"
        # )
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                x_1, y_1 = (
                    BOARD_X_MARGIN + j * CELL_SIZE + CELL_PADDING * j,
                    BOARD_Y_MARGIN + i * CELL_SIZE + CELL_PADDING * i,
                )
                x_2, y_2 = x_1 + CELL_SIZE, y_1 + CELL_SIZE
                gamelib.draw_rectangle(
                    x_1,
                    y_1,
                    x_2,
                    y_2,
                    fill=COLORS.get(value, DEFAULT_CELL_COLOR),
                    outline=COLORS.get(value, DEFAULT_CELL_COLOR),
                )
                if value != EMPTY:
                    gamelib.draw_text(
                        str(value),
                        (x_1 + x_2) / 2,
                        (y_1 + y_2) / 2,
                        fill=NUMBERS_COLOR,
                        bold=True,
                        size=20,
                        font="Helvetica",
                    )

    def new_game_button_clicked(self, x, y):
        """
        Returns True if the new game button was clicked, False otherwise.
        """
        return (
            NEW_GAME_BUTTON[0] <= x <= NEW_GAME_BUTTON[2]
            and NEW_GAME_BUTTON[1] <= y <= NEW_GAME_BUTTON[3]
        )

    def get_random_empty_cell(self):
        """
        Returns a random empty cell from the board. If there are no empty cells, returns False.
        """
        empty_cells = [
            (i, j)
            for i in range(ROWS)
            for j in range(COLUMNS)
            if self.board[i][j] == EMPTY
        ]
        return random.choice(empty_cells) if empty_cells else False

    def insert_random_new_cell(self):
        """
        Inserts a new cell with a value from the possible initial values
        in a random empty cell of the board.
        """
        row, column = self.get_random_empty_cell()
        self.board[row][column] = random.choice(POSSIBLE_INITIAL_VALUES)

    def move_left(self):
        """
        Moves the board to the left, combining the numbers that can be combined
        and moving them to the left.
        """
        changed = False
        for row in range(ROWS):
            if self.combine_row(row):
                changed = True
        return changed

    def combine_row(self, row_index):
        """
        Combines the numbers of a line that can be combined and moves them to the left.
        If there are no combinable numbers, returns the original line.
        """
        row = self.board[row_index]
        combinable_numbers = [number for number in row if number != EMPTY]
        if combinable_numbers:
            result = []
            i = 0
            while i < len(combinable_numbers):
                if (
                    i < len(combinable_numbers) - 1
                    and combinable_numbers[i] == combinable_numbers[i + 1]
                ):
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
        """
        Moves the board to the right, combining the numbers that can
        be combined and moving them to the right.
        """
        self.invert_board()
        changed = self.move_left()
        self.invert_board()
        return changed

    def invert_board(self):
        """
        Inverts the rows of the board.
        """
        self.board = [list(reversed(row)) for row in self.board]

    def transpose_board(self):
        """
        Transposes the rows and columns of the board.
        """
        self.board = [[row[i] for row in self.board] for i in range(COLUMNS)]

    def move_up(self):
        """
        Moves the board to the up, combining the numbers that
        can be combined and moving them to the up.
        """
        self.transpose_board()
        changed = self.move_left()
        self.transpose_board()
        return changed

    def move_down(self):
        """
        Moves the board to the down, combining the numbers that can be
        combined and moving them to the down.
        """
        self.transpose_board()
        changed = self.move_right()
        self.transpose_board()
        return changed

    def update(self, direction):
        """
        Updates the game according to the specified movement in
        the desired direction to move the board.
        """
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
        """
        Returns True if the game is won, False otherwise.
        """
        for i in range(ROWS):
            if WIN_NUMBER in self.board[i]:
                return True
        return False

    def lost(self):
        """
        Returns True if the game is lost, False otherwise.
        """
        if not self.possible_horizontal_moves() and not self.possible_vertical_moves():
            return True
        return False

    def possible_vertical_moves(self):
        """
        Returns True if there are vertical moves possible, False otherwise.
        """
        self.transpose_board()
        result = self.possible_horizontal_moves()
        self.transpose_board()
        return result

    def possible_horizontal_moves(self):
        """
        Returns True if there are horizontal moves possible, False otherwise.
        """
        for i in range(ROWS):
            if self.possible_moves_in_row(self.board[i]):
                return True
        return False

    def possible_moves_in_row(self, row):
        """
        Returns True if there are possible moves in the row, False otherwise.
        """
        i = 0
        while i < len(row):
            if row[i] == EMPTY:
                return True
            if i < len(row) - 1 and row[i] == row[i + 1]:
                return True
            i += 1
        return False
