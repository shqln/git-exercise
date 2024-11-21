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
BLUE = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (WINDOW_X//10)) * 10, 
                  random.randrange(1, (WINDOW_Y//10)) * 10]

fruit_exists = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):
  
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():
  
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, RED)
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (WINDOW_X/2, WINDOW_Y/4)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # after 2 seconds we will quit the program
    time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()


# Main Function
while True:
    
    # handling key events
    for event in pygame.event.get():
        # TODO 1: complete the movement commands
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_over()
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            

    # If two keys pressed simultaneously
    # we don't want snake to move into two 
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # TODO 2: complete the movements
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    # TODO 3: score is not incrementing, something is missing....
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        fruit_exists = False
    else:
        snake_body.pop()
        
    if not fruit_exists:
        fruit_position = [random.randrange(1, (WINDOW_X//10)) * 10, 
                          random.randrange(1, (WINDOW_Y//10)) * 10]
        
    fruit_exists = True
    game_window.fill(BLACK)
    
    # TODO 4: snakes should be green! let's make the window white too.
    for pos in snake_body:
        pygame.draw.rect(game_window, WHITE,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, BLUE, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))


    # TODO 5: complete the game over conditions
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > WINDOW_X-10:
        pass
    if snake_position[1] < 0 or snake_position[1] > WINDOW_Y-10:
        pass

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, WHITE, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(SNAKE_SPEED)

    
    
# TODO optional A: increase the speed of the snake every time it eats a fruit
# TODO optional B: change the color of the snake to a gradient.