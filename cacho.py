import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Cacho")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 150, 144)

# Fuentes
font = pygame.font.SysFont(None, 36)
font_small = pygame.font.SysFont(None, 24)

# Dados
dice_images = [pygame.Surface((100, 100)) for _ in range(6)]
for i in range(6):
    dice_images[i].fill(WHITE)
    pygame.draw.rect(dice_images[i], BLACK, dice_images[i].get_rect(), 5)
    # Agregar puntos en el dado
    if i == 0:
        pygame.draw.circle(dice_images[i], BLACK, (50, 50), 10)
    elif i == 1:
        pygame.draw.circle(dice_images[i], BLACK, (25, 25), 10)
        pygame.draw.circle(dice_images[i], BLACK, (75, 75), 10)
    elif i == 2:
        pygame.draw.circle(dice_images[i], BLACK, (25, 25), 10)
        pygame.draw.circle(dice_images[i], BLACK, (50, 50), 10)
        pygame.draw.circle(dice_images[i], BLACK, (75, 75), 10)
    elif i == 3:
        pygame.draw.circle(dice_images[i], BLACK, (25, 25), 10)
        pygame.draw.circle(dice_images[i], BLACK, (25, 75), 10)
        pygame.draw.circle(dice_images[i], BLACK, (75, 25), 10)
        pygame.draw.circle(dice_images[i], BLACK, (75, 75), 10)
    elif i == 4:
        pygame.draw.circle(dice_images[i], BLACK, (25, 25), 10)
        pygame.draw.circle(dice_images[i], BLACK, (25, 75), 10)
        pygame.draw.circle(dice_images[i], BLACK, (75, 25), 10)
        pygame.draw.circle(dice_images[i], BLACK, (75, 75), 10)
        pygame.draw.circle(dice_images[i], BLACK, (50, 50), 10)
    elif i == 5:
        pygame.draw.circle(dice_images[i], BLACK, (25, 25), 10)
        pygame.draw.circle(dice_images[i], BLACK, (25, 75), 10)
        pygame.draw.circle(dice_images[i], BLACK, (75, 25), 10)
        pygame.draw.circle(dice_images[i], BLACK, (75, 75), 10)
        pygame.draw.circle(dice_images[i], BLACK, (50, 50), 10)
        pygame.draw.circle(dice_images[i], BLACK, (50, 25), 10)

# Función para tirar los dados
def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

# Función para mostrar los dados en la pantalla
def draw_dice(dice, x, y):
    for i, die in enumerate(dice):
        screen.blit(dice_images[die - 1], (x + i * 120, y))

# Función para obtener la jugada y la puntuación según reglas
def get_jugada_and_score(dice):
    counts = [dice.count(i) for i in range(1, 7)]
    
    # Verificar combinaciones especiales
    unique_values = sorted(set(dice))
    
    # Escalera: [1, 2, 3, 4, 5] o [2, 3, 4, 5, 6]
    if unique_values == [1, 2, 3, 4, 5] or unique_values == [2, 3, 4, 5, 6]:
        return "Escalera", 25

    # Full: tres iguales y dos iguales
    if 3 in counts and 2 in counts:
        return "Full", 35

    # Póker: cuatro iguales
    if 4 in counts:
        return "Póker", 45

    # Elegir la jugada de mayor frecuencia
    max_count = max(counts)
    max_value = counts.index(max_count) + 1  # Ajustar índice para los números de 1 a 6
    
    # Asignar nombres y calcular puntos según el número mayormente repetido
    if max_value == 1:
        return f"Balas ({max_count})", max_count * 1
    elif max_value == 2:
        return f"Tontos ({max_count})", max_count * 2
    elif max_value == 3:
        return f"Trenes ({max_count})", max_count * 3
    elif max_value == 4:
        return f"Cuadras ({max_count})", max_count * 4
    elif max_value == 5:
        return f"Quinas ({max_count})", max_count * 5
    elif max_value == 6:
        return f"Señas ({max_count})", max_count * 6

    return "Nada", 0

# Función para mostrar texto en la pantalla
def draw_text(text, x, y, color=BLACK, font=font):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Función para mostrar las opciones de jugadas en forma vertical
def draw_jugada_options(dice):
    options = ["Balas", "Tontos", "Trenes", "Cuadras", "Quinas", "Señas", "Escalera", "Full", "Póker"]
    jugada, _ = get_jugada_and_score(dice)
    
    # Mostrar las opciones de jugadas en formato vertical
    draw_text("Opciones de Jugada:", 50, 500, BLACK, font)
    for i, option in enumerate(options):
        draw_text(f"{i+1}. {option}", 50, 530 + i * 30, BLACK, font_small)

# Función para el turno del jugador
def player_turn():
    dice = roll_dice()
    jugada, score = get_jugada_and_score(dice)
    return dice, jugada, score

# Función para el turno de la computadora
def computer_turn():
    dice = roll_dice()
    jugada, score = get_jugada_and_score(dice)
    return dice, jugada, score

# Función principal del juego
def main():
    player_scores = [0] * 5
    computer_scores = [0] * 5
    game_over = False
    turn = 'player'
    player_turns = 0
    computer_turns = 0

    while True:
        screen.fill(LIGHT_BLUE)

        if game_over:
            winner = "Jugador" if sum(player_scores) > sum(computer_scores) else "Computadora"
            draw_text(f"¡{winner} gana! Presiona Q para salir.", 250, 250, RED)
            draw_text(f"Tu puntaje total es: {sum(player_scores)}", 250, 280, RED)
            draw_text(f"Puntaje total Computadora: {sum(computer_scores)}", 250, 310, RED)
        
        if turn == 'player' and player_turns < 5:
            draw_text(f"Tu turno. ¡Presiona Enter para tirar los dados!", 200, 150)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        player_dice = roll_dice()
                        draw_dice(player_dice, 200, 300)
                        draw_jugada_options(player_dice)
                        pygame.display.flip()

                        # Esperar a que el jugador elija la jugada
                        waiting_for_choice = True
                        while waiting_for_choice:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_1:  # Elección de jugada por tecla
                                        player_scores[player_turns] = player_dice.count(1) * 1
                                        draw_text(f"Has ganado {player_scores[player_turns]} puntos con Balas.", 200, 450, LIGHT_GREEN)
                                        waiting_for_choice = False
                                    elif event.key == pygame.K_2:
                                        player_scores[player_turns] = player_dice.count(2) * 2
                                        draw_text(f"Has ganado {player_scores[player_turns]} puntos con Tontos.", 200, 450, LIGHT_GREEN)
                                        waiting_for_choice = False
                                    elif event.key == pygame.K_3:
                                        player_scores[player_turns] = player_dice.count(3) * 3
                                        draw_text(f"Has ganado {player_scores[player_turns]} puntos con Trenes.", 200, 450, LIGHT_GREEN)
                                        waiting_for_choice = False
                                    elif event.key == pygame.K_4:
                                        player_scores[player_turns] = player_dice.count(4) * 4
                                        draw_text(f"Has ganado {player_scores[player_turns]} puntos con Cuadras.", 200, 450, LIGHT_GREEN)
                                        waiting_for_choice = False
                                    elif event.key == pygame.K_5:
                                        player_scores[player_turns] = player_dice.count(5) * 5
                                        draw_text(f"Has ganado {player_scores[player_turns]} puntos con Quinas.", 200, 450, LIGHT_GREEN)
                                        waiting_for_choice = False
                                    elif event.key == pygame.K_6:
                                        player_scores[player_turns] = player_dice.count(6) * 6
                                        draw_text(f"Has ganado {player_scores[player_turns]} puntos con Señas.", 200, 450, LIGHT_GREEN)
                                        waiting_for_choice = False
                                    elif event.key == pygame.K_e:
                                        player_scores[player_turns] = 25  # Escalera
                                        draw_text(f"Has ganado 25 puntos con Escalera.", 200, 450, LIGHT_GREEN)
                                        waiting_for_choice = False
                                    elif event.key == pygame.K_f:
                                        player_scores[player_turns] = 35  # Full
                                        draw_text(f"Has ganado 35 puntos con Full.", 200, 450, LIGHT_GREEN)
                                        waiting_for_choice = False
                                    elif event.key == pygame.K_p:
                                        player_scores[player_turns] = 45  # Póker
                                        draw_text(f"Has ganado 45 puntos con Póker.", 200, 450, LIGHT_GREEN)
                                        waiting_for_choice = False

                        player_turns += 1
                        turn = 'computer'
                        break

        elif turn == 'computer' and computer_turns < 5:
            pygame.time.wait(1000)
            computer_dice, computer_jugada, computer_score = computer_turn()
            computer_scores[computer_turns] = computer_score
            draw_dice(computer_dice, 200, 300)
            draw_text(f"Jugada: {computer_jugada}", 200, 450, LIGHT_GREEN)
            draw_text(f"Puntuación: {computer_score}", 200, 480, LIGHT_GREEN)
            pygame.display.flip()

            # Esperar a que el jugador presione Enter para pasar al turno del jugador
            waiting_for_next_turn = True
            while waiting_for_next_turn:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            waiting_for_next_turn = False
            computer_turns += 1
            turn = 'player'

        if player_turns >= 5 and computer_turns >= 5:
            game_over = True
            draw_text(f"Juego terminado. Puntaje final: Jugador {sum(player_scores)} - Computadora {sum(computer_scores)}", 150, 200)
            pygame.display.flip()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q and game_over:
                pygame.quit()
                sys.exit()

# Ejecutar el juego
if __name__ == "__main__":
    main()
