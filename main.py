import gamelib as gamelib
import logic
from constants import UP, DOWN, LEFT, RIGHT

'''
def main():
    juego = logica.inicializar_juego()
    while True:
        logica.mostrar_juego(juego)
        if logica.juego_ganado(juego):
            print("Felicidades! Sos lo mas")
            return
        if logica.juego_perdido(juego):
            print("Lola, volve a intentar")
            return
        dir = logica.pedir_direccion(juego)
        nuevo_juego = logica.actualizar_juego(juego, dir)
        if nuevo_juego != juego:
            juego = logica.insertar_nuevo_random(nuevo_juego)
'''

def main():
    gamelib.resize(800, 500)
    gamelib.title("2048")
    gamelib.draw_rectangle(0, 0, 800, 500, fill="white")
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
