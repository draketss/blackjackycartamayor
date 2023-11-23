# main.py
from blackjack import JuegoBlackjack

if __name__ == "__main__":
    nombre_jugador1 = input("Ingresa el nombre del Jugador 1: ")
    nombre_jugador2 = input("Ingresa el nombre del Jugador 2: ")
    num_rondas = int(input("Ingresa el número de rondas a jugar: "))

    juego_blackjack = JuegoBlackjack(nombre_jugador1, nombre_jugador2, num_rondas)
    juego_blackjack.jugar()
