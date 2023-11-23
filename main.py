# main.py
from baraja import BarajaInglesa

if __name__ == "__main__":
    # Solicitar nombres de jugadores y número de rondas
    nombre_jugador1 = input("Ingresa el nombre del Jugador 1: ")
    nombre_jugador2 = input("Ingresa el nombre del Jugador 2: ")
    num_rondas = int(input("Ingresa el número de rondas a jugar: "))

    # Crear instancia del juego y jugar
    juego = BarajaInglesa(nombre_jugador1, nombre_jugador2, num_rondas)
    juego.jugar()
    
    # Mostrar resultados al final del juego
    juego.mostrar_resultados()
