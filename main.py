import gamelib as gamelib
from logic import Game
from constants import UP, DOWN, LEFT, RIGHT, BACKGROUND_COLOR


def main():
    gamelib.resize(800, 600)
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
        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break
        game.update(ev.key)

        
gamelib.init(main)
