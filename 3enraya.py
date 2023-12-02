'''Juego Tres en Raya - Jugador vs. Máquina'''

import random
import time
import os


def presentacion_1():

    '''Devuelve el nivel en el que quiere jugar el usuario'''

    print()
    print("{:^50}".format("TRES EN RAYA"))
    print()
    print()
    print("1. Fácil")
    print("2. Difícil")
    print()
    print("Escoger una dificultad:")
    print()

    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel = input("--> ")

    return int(nivel)


def presentacion_2():

    '''Devuelve la ficha elegida por el usuario y la ficha del ordenador'''

    print()
    print("{:^50}".format("TRES EN RAYA"))
    print()
    print()
    print("Empieza la ficha O")
    print()
    print("Elige: O / X")
    print()
    print()

    ficha = ""
    while ficha != "O" and ficha != "X":
        ficha = input("--> ").upper()

    if ficha == "O":
        humano = "O"
        ordenador = "X"
    else:
        humano = "X"
        ordenador = "O"

    return humano, ordenador


def mostrar_tablero(tablero):

    '''Muestra el tablero de juego con las casillas vacías y las fichas puestas'''

    print()
    print("{:^47}".format("TRES EN RAYA"))
    print()
    print("         1        |2        |3")
    print("             {}    |    {}    |    {}".format(tablero[0], tablero[1], tablero[2]))
    print("                  |         |")
    print("         ---------+---------+---------")
    print("         4        |5        |6")
    print("             {}    |    {}    |    {}".format(tablero[3], tablero[4], tablero[5]))
    print("                  |         |")
    print("         ---------+---------+---------")
    print("         7        |8        |9")
    print("             {}    |    {}    |    {}".format(tablero[6], tablero[7], tablero[8]))
    print("                  |         |")
    print()


def seguir_jugando():

    '''Devuelve True si el usuario quiere jugar otra partida, sino devuelve False'''

    print()
    respuesta = input("¿Jugar otra partida? ").lower()
    if respuesta == "s" or respuesta == "si":
        return True
    else:
        return False


def hay_ganador(tablero, jugador):

    '''Comprueba si un estado del tablero es ganador: Tiene tres fichas en raya'''

    if  tablero[0] == tablero[1] == tablero[2] == jugador or \
        tablero[3] == tablero[4] == tablero[5] == jugador or \
        tablero[6] == tablero[7] == tablero[8] == jugador or \
        tablero[0] == tablero[3] == tablero[6] == jugador or \
        tablero[1] == tablero[4] == tablero[7] == jugador or \
        tablero[2] == tablero[5] == tablero[8] == jugador or \
        tablero[0] == tablero[4] == tablero[8] == jugador or \
        tablero[2] == tablero[4] == tablero[6] == jugador:
        return True
    else:
        return False


def tablero_lleno(tablero):

    '''Devuelve True si el tablero está lleno y False si quedan casillas vacías'''

    for i in tablero:
        if i == " ":
            return False
    else:
        return True


def casilla_libre(tablero, casilla):

    '''Devuelve True si una casilla dada está vacía y False si está llena'''

    return tablero[casilla] == " "


def movimiento_jugador(tablero):

    '''Devuelve la casilla elegida por el jugador humano'''

    posiciones = ["1","2","3","4","5","6","7","8","9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input(("{:^47}".format("Escoger un número entre (1 - 9)")))

        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion - 1):
                print("{:^47}".format("Esta posición está ocupada"))
            else:
                return posicion - 1


def mov_ordenador_facil(tablero, jugador):

    '''El ordenador sólo se defiende de ser ganado en la siguiente jugada'''

    for i in range(9):
        copia = list(tablero)
        if casilla_libre(copia, i):
            copia[i] = jugador
            if hay_ganador(copia, jugador):
                return i
    while True:
        casilla = random.randint(0,8)
        if not casilla_libre(tablero, casilla):
            casilla = random.randint(0,8)
        else:
            return casilla


def mov_ordenador_dificil(tablero, maquina, usuario):

    '''Primero trata de ganar, luego evita ser ganado. Sino, si mueve segundo
       el ordenador intenta coger la casilla del medio, sino una esquina.
       Si sale primero el ordenador, el primer movimiento e aleatorio, pero
       en el segundo trata de coger la casilla del medio si está libre.'''

    for i in range(9):
        copia = list(tablero)
        if casilla_libre(copia, i):
            copia[i] = maquina
            if hay_ganador(copia, maquina):
                return i

    for i in range(9):
        copia = list(tablero)
        if casilla_libre(copia, i):
            copia[i] = usuario
            if hay_ganador(copia, usuario):
                return i

    if ordenador == "X":
        if tablero[4] == " ":
            return 4
        esquinas_vacias = []
        for i in [0, 2, 6, 8]:
            if casilla_libre(tablero, i):
                esquinas_vacias.append(i)
        demas_vacias = []
        for i in [1, 3, 5, 7]:
            if casilla_libre(tablero, i):
                demas_vacias.append(i)
        if len(esquinas_vacias) < 0:
            return random.choice(esquinas_vacias)
        else:
            return random.choice(demas_vacias)

    if ordenador == "O":
        contador = 0
        for i in range(9):
            if casilla_libre(tablero, i):
                contador += 1
        if contador == 7:
            if tablero[4] == " ":
                return 4

    while True:
        casilla = random.randint(0,8)
        if not casilla_libre(tablero, casilla):
            casilla = random.randint(0,8)
        else:
            return casilla


'''#################### PROGRAMA PRINCIPAL ####################'''

jugando = True

while jugando:

    tablero = [" "] * 9

    os.system("cls")

    nivel = presentacion_1()

    os.system("cls")

    humano, ordenador = presentacion_2()

    os.system("cls")

    mostrar_tablero(tablero)

    if humano == "O":
        turno = "Humano"
    else:
        turno = "Ordenador"

    partida = True

    while partida:

        if tablero_lleno(tablero):
            print("{:^47}".format("Empate"))
            partida = False

        elif turno == "Humano":
            casilla = movimiento_jugador(tablero)
            tablero[casilla] = humano
            turno = "Ordenador"
            os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero, humano):
                print("{:^47}".format("Has ganado"))
                partida = False

        elif turno == "Ordenador":
            print("{:^47}".format("El ordenador está pensando ..."))
            time.sleep(2)
            if nivel == 1:
                casilla = mov_ordenador_facil(tablero, humano)
            elif nivel == 2:
                casilla = mov_ordenador_dificil(tablero, ordenador, humano)
            tablero[casilla] = ordenador
            turno = "Humano"
            os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero, ordenador):
                print("{:^47}".format("Has perdido"))
                partida = False

    jugando = seguir_jugando()