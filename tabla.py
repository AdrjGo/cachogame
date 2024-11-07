import pygame
import sys
from dados import lanzar_dados, obtenet_valores_actuales

# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
GREEN = (45, 87, 44)
GRAY = (100, 100, 100)

# Dimensiones de la pantalla
WIDTH, HEIGHT = 600, 400
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

# Función para dibujar una cuadrícula 3x3
def draw_grid(position):
    x, y = position
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(x + col * CELL_SIZE, y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 2)

# Función para dibujar los dados con sus valores actuales
def draw_dice(positions):
    dice_values = obtenet_valores_actuales()
    for i, pos in enumerate(positions):
        rect = pygame.Rect(pos[0], pos[1], DICE_SIZE, DICE_SIZE)
        pygame.draw.rect(screen, WHITE, rect, 2)
        dice_text = font.render(str(dice_values[i]), True, WHITE)
        screen.blit(dice_text, (pos[0] + DICE_SIZE // 4, pos[1] + DICE_SIZE // 4))

# Bucle principal del juego
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
