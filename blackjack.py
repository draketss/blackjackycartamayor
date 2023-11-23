import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.partidas_ganadas = 0

    def recibir_carta(self, carta, valor):
        self.puntos += valor
        print(f'{self.nombre} recibe: {carta}')

class JuegoBlackjack:
    def __init__(self, nombre_jugador1, nombre_jugador2, num_rondas):
        self.jugador1 = Jugador(nombre_jugador1)
        self.jugador2 = Jugador(nombre_jugador2)
        self.num_rondas = num_rondas
        self.palos = ['Corazon', 'Trebol', 'Diamante', 'Picas']
        self.cartas = {'Dos': 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5, 'Seis': 6, 'Siete': 7, 'Ocho': 8, 'Nueve': 9, 'Diez': 10, 'Jota': 10, 'Reina': 10, 'Rey': 10, 'As': 11}

    def repartir_cartas(self):
        carta = random.choice(list(self.cartas))
        palo = random.choice(self.palos)
        valor = self.cartas[carta]
        return f'{carta} de {palo}', valor

    def jugar_ronda(self):
        print('--- Rondas ---')

        # Reiniciar los puntos de los jugadores al comienzo de cada ronda
        self.jugador1.puntos = 0
        self.jugador2.puntos = 0

        # Repartir dos cartas a cada jugador
        for jugador in [self.jugador1, self.jugador2]:
            carta, valor = self.repartir_cartas()
            jugador.recibir_carta(carta, valor)

        print('--- Resultados de la Ronda ---')
        print(f'{self.jugador1.nombre}: {self.jugador1.puntos} puntos')
        print(f'{self.jugador2.nombre}: {self.jugador2.puntos} puntos')

        # Turno del Jugador 1
        while self.jugador1.puntos <= 16:
            carta, valor = self.repartir_cartas()
            self.jugador1.recibir_carta(carta, valor)

        # Turno del Jugador 2
        while self.jugador2.puntos <= 16:
            carta, valor = self.repartir_cartas()
            self.jugador2.recibir_carta(carta, valor)

        # Determinar el ganador de la ronda
        ganador = self.determinar_ganador_ronda()
        if ganador:
            print(f'{ganador.nombre} gana la ronda!')
            ganador.partidas_ganadas += 1
        else:
            print('Empate.')

    def determinar_ganador_ronda(self):
        if self.jugador1.puntos > 21 and self.jugador2.puntos > 21:
            return None  # Ambos jugadores han superado 21 puntos, es un empate
        elif self.jugador1.puntos <= 21 and (self.jugador2.puntos > 21 or self.jugador1.puntos > self.jugador2.puntos):
            return self.jugador1
        elif self.jugador2.puntos <= 21 and (self.jugador1.puntos > 21 or self.jugador2.puntos > self.jugador1.puntos):
            return self.jugador2
        else:
            return None  # Ningún jugador gana, es un empate

    def mostrar_resultados(self):
        print('--- Resultados Finales ---')
        print(f'{self.jugador1.nombre}: {self.jugador1.partidas_ganadas} partidas ganadas, felicidades!!')
        print(f'{self.jugador2.nombre}: {self.jugador2.partidas_ganadas} partidas ganadas, felicidades!!')

        # Determinar el ganador final
        if self.jugador1.partidas_ganadas > self.jugador2.partidas_ganadas:
            print(f'¡{self.jugador1.nombre} es el ganador del juego!!')
        elif self.jugador2.partidas_ganadas > self.jugador1.partidas_ganadas:
            print(f'¡{self.jugador2.nombre} es el ganador del juego!!')
        else:
            print('Empate.')

    def jugar(self):
        for _ in range(self.num_rondas):
            self.jugar_ronda()

        # Mostrar resultados al final del juego
        self.mostrar_resultados()
