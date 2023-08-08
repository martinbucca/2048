"""
This module contains the main function of the game. It initializes the game and runs the game loop.
"""
import gamelib
from logic import Game


def main():
    '''
    Main function. Initializes the game and runs the game loop.
    '''
    gamelib.resize(600, 600)
    gamelib.title("2048")
    game = Game()
    while gamelib.is_alive():
        if game.won():
            gamelib.say("You won!")
            game.reset()
        if game.lost():
            gamelib.say("You lost!")
            game.reset()
        game.show()
        event = gamelib.wait()
        if not event:
            break
        if event.type == gamelib.EventType.KeyPress:
            game.update(event.key)
        elif event.type == gamelib.EventType.ButtonPress and event.mouse_button == 1 and game.new_game_button_clicked(event.x, event.y):
            game.reset()


gamelib.init(main)
