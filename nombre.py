# player_logic.py
import random

# Lista de posibles nombres para la máquina
computer_names = ["Hal", "R2-D2", "T-800", "C3PO", "Jarvis", "WALL-E"]

# Función para obtener el nombre del jugador humano
def nombre_humano():

    nombre = input("Ingresa tu nombre: ")
    if nombre not in computer_names:
        return "Jugador Humano"
    else:
        return nombre

# Función para obtener un nombre aleatorio para la máquina
def nombre_computador():
    return random.choice(computer_names)
