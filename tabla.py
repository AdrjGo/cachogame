import pygame
import sys
import random
from dados import lanzar_dados, obtener_valores_actuales
from nombre import nombre_humano, nombre_computador

# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
GREEN = (45, 87, 44)
GRAY = (100, 100, 100)

# Dimensiones de la pantalla
WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Cacho")

# Configuración de fuentes
font = pygame.font.Font(None, 36)

# Posiciones y dimensiones para los cuadros 3x3
GRID_SIZE = 3
CELL_SIZE = 40
GRID_MARGIN = 100
PLAYER_GRID_POS = (GRID_MARGIN, GRID_MARGIN)
COMPUTER_GRID_POS = (WIDTH - GRID_MARGIN - GRID_SIZE * CELL_SIZE, GRID_MARGIN)

# Tamaño de cada dado
DICE_SIZE = 40
DICE_MARGIN = 10  # Espacio entre dados

# Posición y dimensiones del botón (más ancho)
BUTTON_WIDTH, BUTTON_HEIGHT = 180, 40
button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT - BUTTON_HEIGHT - 20), (BUTTON_WIDTH, BUTTON_HEIGHT))

# Lista de nombres posibles para la máquina
nombres_maquina = ["HAL 9000", "R2-D2", "C-3PO", "Skynet", "WALL-E", "Jarvis", "Optimus Prime"]

# Función para obtener el nombre de la máquina
def generar_nombre_maquina():
    return random.choice(nombres_maquina)

# Función para dibujar una cuadrícula 3x3
def draw_grid(position):
    x, y = position
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(x + col * CELL_SIZE, y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 2)

# Función para dibujar los dados con sus valores actuales
def draw_dice(positions):
    dice_values = obtener_valores_actuales()
    for i, pos in enumerate(positions):
        rect = pygame.Rect(pos[0], pos[1], DICE_SIZE, DICE_SIZE)
        pygame.draw.rect(screen, WHITE, rect, 2)
        dice_text = font.render(str(dice_values[i]), True, WHITE)
        screen.blit(dice_text, (pos[0] + DICE_SIZE // 4, pos[1] + DICE_SIZE // 4))

# Función para dibujar los nombres de los jugadores
def draw_player_names():
    player_name_text = font.render(f"Jugador: {nombre_humano}", True, WHITE)
    computer_name_text = font.render(f"Máquina: {nombre_computador}", True, WHITE)
    screen.blit(player_name_text, (20, 20))
    screen.blit(computer_name_text, (WIDTH - 200, 20))

# Función para manejar la entrada del nombre del jugador
def obtener_nombre_jugador():
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 30, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text  
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(GREEN)
        txt_surface = font.render(text, True, WHITE)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)

# Bucle principal del juego
def main():
    global nombre_humano, nombre_computador

    # Pedir el nombre del jugador
    nombre_humano = obtener_nombre_jugador()
    nombre_computador = generar_nombre_maquina()

    # Bucle del juego
    running = True
    while running:
        screen.fill(GREEN)

        # Dibujar los cuadros 3x3 para el jugador y la computadora
        draw_grid(PLAYER_GRID_POS)
        draw_grid(COMPUTER_GRID_POS)

        # Posiciones de los dados
        start_x_top = WIDTH // 2 - (DICE_SIZE + DICE_MARGIN) - 20
        top_dice_positions = [(start_x_top + i * (DICE_SIZE + DICE_MARGIN), HEIGHT // 2 - DICE_SIZE) for i in range(3)]
        start_x_bottom = WIDTH // 2 - (DICE_SIZE + DICE_MARGIN // 2)
        bottom_dice_positions = [(start_x_bottom + i * (DICE_SIZE + DICE_MARGIN), HEIGHT // 2 + DICE_SIZE // 2) for i in range(2)]
        dice_positions = top_dice_positions + bottom_dice_positions

        # Dibujar los dados y sus valores actuales
        draw_dice(dice_positions)

        # Dibujar el botón de "Lanzar dados"
        pygame.draw.rect(screen, GRAY, button_rect)
        button_text = font.render("Lanzar dados", True, WHITE)
        screen.blit(button_text, (button_rect.x + 10, button_rect.y + 5))

        # Dibujar los nombres de los jugadores
        draw_player_names()

        # Evento de cierre y clic del botón
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    lanzar_dados()  # Lanza los dados al hacer clic en el botón

        # Actualizar la pantalla
        pygame.display.flip()

    # Salir de Pygame
    pygame.quit()
    sys.exit()

# Iniciar el juego
if __name__ == "__main__":
    main()
