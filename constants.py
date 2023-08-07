"""
This module contains the constants used in the game.
"""
# GRAPHICS CONSTANTS
SCORE_LABEL_POSITION = (300, 30)
SCORE_POSITION = (300, 70)
CELL_SIZE = 100
BOARD_X_MARGIN = 100
BOARD_Y_MARGIN = 100
# GAME CONSTANTS
WIN_NUMBER = 2048
INITIAL_SCORE = 0
POSSIBLE_INITIAL_VALUES = (2, 4)
ROWS = 4
COLUMNS = 4
# DIRECTIONS
UP = "Up"
RIGHT = "Right"
DOWN = "Down"
LEFT = "Left"
EMPTY = 0
# FORMATTING CONSTANTS
BACKGROUND_COLOR = "#444444"
DEFAULT_CELL_COLOR = "#bbbbbb"
NUMBERS_COLOR = "black"
COLORS = {
    2: "#fdefe8",  # Rosa claro
    4: "#fad2d7",  # Rosa pálido
    8: "#f59eb1",  # Rosa medio
    16: "#ff6f91",  # Rosa fuerte
    32: "#f984a1",  # Rosa oscuro
    64: "#f8818a",  # Rosa intenso
    128: "#e6f1f8",  # Celeste claro
    256: "#94c2e5",  # Azul cielo
    512: "#f368e0",  # Rosa violeta
    1024: "#81b5e9",  # Azul pastel
    2048: "#073a6e",  # Azul brillante
}
