import gamelib as gamelib
import logic
from constants import UP, DOWN, LEFT, RIGHT, BACKGROUND_COLOR


def main():
    gamelib.resize(800, 600)
    gamelib.title("2048")
    gamelib.draw_rectangle(0, 0, 800, 600, fill=BACKGROUND_COLOR)
    gamelib.draw_text("Score", 400, 20, size=30, fill="white")
    board = logic.initialize_2048()
    while gamelib.is_alive():
        if logic.won_game(board):
            gamelib.say("You won!")
            break
        if logic.lost_game(board):
            gamelib.say("You lost!")
            break
        logic.show_ui(board)
        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break
        updated_board = logic.update_game(board, ev.key)
        if updated_board != board:
            board = logic.insert_random_new_cell(updated_board)

        
gamelib.init(main)
