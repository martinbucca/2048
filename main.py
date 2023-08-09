"""
This module contains the main function of the game. It initializes the game and runs the game loop.
"""
import gamelib
from logic import Game


def main():
    """
    Main function. Initializes the game and runs the game loop.
    """
    gamelib.resize(600, 600)
    gamelib.title("2048")
    game = Game()
    while gamelib.is_alive():
        game.show()
        if game.lost() or game.won():
            message = "You won!" if game.won() else "You lost!"
            gamelib.say(message)
            game.reset()
            continue
        event = gamelib.wait()
        if not event:
            game.store_best_score()
            break
        if event.type == gamelib.EventType.KeyPress:
            game.update(event.key)
        elif (
            event.type == gamelib.EventType.ButtonPress
            and event.mouse_button == 1
            and game.new_game_button_clicked(event.x, event.y)
        ):
            game.reset()


gamelib.init(main)
