
# game_logic.py
import random

# Variables para almacenar los valores de los dados
dice_values = [1, 1, 1, 1, 1]

# Función para lanzar los dados y obtener valores aleatorios
def lanzar_dados():
    global dice_values
    dice_values = [random.randint(1, 6) for _ in range(5)]
    return dice_values

# Función para obtener los valores actuales de los dados
def obtenet_valores_actuales():
    return dice_values
