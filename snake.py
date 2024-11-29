# importing libraries
import pygame
import time
import random

SNAKE_SPEED = 15

# Window size
WINDOW_X = 720
WINDOW_Y = 480

# defining colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Initialize game variables
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
fruit_position = [random.randrange(1, (WINDOW_X//10)) * 10,
                  random.randrange(1, (WINDOW_Y//10)) * 10]
fruit_exists = True
direction = 'RIGHT'
change_to = direction
score = 0

# Function to reset the game
def reset_game():
    global snake_position, snake_body, fruit_position, fruit_exists, direction, change_to, score
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(1, (WINDOW_X//10)) * 10,
                      random.randrange(1, (WINDOW_Y//10)) * 10]
    fruit_exists = True
    direction = 'RIGHT'
    change_to = direction
    score = 0

# Function to display the score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score) + '. Press R to Restart', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WINDOW_X/2, WINDOW_Y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart game
                    return
                if event.key == pygame.K_q:  # Quit game
                    pygame.quit()
                    quit()

# Main game function
def run_game():
    global direction, change_to, snake_position, snake_body, fruit_exists, fruit_position, score

    while True:
        # Handle key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # Ensure snake doesn't move in the opposite direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Move the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_exists = False
        else:
            snake_body.pop()

        if not fruit_exists:
            fruit_position = [random.randrange(1, (WINDOW_X//10)) * 10,
                              random.randrange(1, (WINDOW_Y//10)) * 10]
        fruit_exists = True

        # Clear screen
        game_window.fill(BLACK)

        # Draw snake body
        for pos in snake_body:
            pygame.draw.rect(game_window, GREEN,
                             pygame.Rect(pos[0], pos[1], 10, 10))
        
        # Draw fruit
        pygame.draw.rect(game_window, RED, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        # Game over conditions
        if (snake_position[0] < 0 or snake_position[0] > WINDOW_X-10 or
                snake_position[1] < 0 or snake_position[1] > WINDOW_Y-10):
            game_over()
            return

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
                return

        # Display the score
        show_score(1, WHITE, 'times new roman', 20)

        # Refresh game screen
        pygame.display.update()

        # Refresh rate
        fps.tick(SNAKE_SPEED)

# Main loop
while True:
    reset_game()
    run_game()
