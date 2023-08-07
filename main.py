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
            break
        if game.lost():
            gamelib.say("You lost!")
            break
        game.show()
        event = gamelib.wait(gamelib.EventType.KeyPress)
        if not event:
            break
        game.update(event.key)


gamelib.init(main)
