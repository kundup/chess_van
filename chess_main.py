import pygame
import random

# initializing
pygame.init()

# constants
screen_width = 640
screen_height = 640
game_title = "chess_van"

# display
screen = pygame.display.set_mode((screen_width, screen_height))
game_name = pygame.display.set_caption(game_title)


# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()


pygame.quit()
