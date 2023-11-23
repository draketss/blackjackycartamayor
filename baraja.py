import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.juegos_ganados = 0

class BarajaInglesa:
    def __init__(self, nombre_jugador1, nombre_jugador2, num_rondas):
        # Crear jugadores
        self.jugador1 = Jugador(nombre_jugador1)
        self.jugador2 = Jugador(nombre_jugador2)
        # Otras inicializaciones
        self.nombres_cartas = ['As', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez', 'Jota', 'Reina', 'Rey']
        # Número de rondas
        self.num_rondas = num_rondas

    def jugar_ronda(self):
        # Lógica para jugar una ronda
        carta_jugador1 = random.randint(1, 13)
        carta_jugador2 = random.randint(1, 13)
        
        print('--- Rondas --- ')
        print(f'{self.jugador1.nombre}: {self.nombres_cartas[carta_jugador1 - 1]} vs {self.jugador2.nombre}: {self.nombres_cartas[carta_jugador2 - 1]}')

        # Agrega esto para manejar el caso de empate
        if carta_jugador1 == carta_jugador2:
            print('Empate, nadie gana la ronda.')
            return

        if carta_jugador1 > carta_jugador2:
            print(f'{self.jugador1.nombre} gana la ronda')
            self.jugador1.juegos_ganados += 1
        else:
            print(f'{self.jugador2.nombre} gana la ronda')
            self.jugador2.juegos_ganados += 1

    def mostrar_resultados(self):
        # Mostrar resultados finales
        print('--- Resultados finales ---')
        print(f'{self.jugador1.nombre}: {self.jugador1.juegos_ganados} juegos ganados, felicidades!!')
        print(f'{self.jugador2.nombre}: {self.jugador2.juegos_ganados} juegos ganados, felicidades!!')

        if self.jugador1.juegos_ganados > self.jugador2.juegos_ganados:
            print(f'{self.jugador1.nombre} es el ganador del juego!')
        elif self.jugador2.juegos_ganados > self.jugador1.juegos_ganados:
            print(f'{self.jugador2.nombre} es el ganador del juego!')
        else:
            print('Empate en el juego.')

    def jugar(self):
        # Bucle para jugar las rondas especificadas
        for _ in range(self.num_rondas):
            self.jugar_ronda()
