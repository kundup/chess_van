import pygame
import random

# initializing
pygame.init()

# constants
screen_width = 640
screen_height = 640
game_title = "chess_van"
size = 60

# display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_title)

# images
black_bishop = pygame.transform.scale(pygame.image.load("b_bishop.png").convert_alpha(), (size, size))
black_king = pygame.transform.scale(pygame.image.load("b_king.png").convert_alpha(), (size, size))
black_knight = pygame.transform.scale(pygame.image.load("b_knight.png").convert_alpha(), (size, size))
black_pawn = pygame.transform.scale(pygame.image.load("b_pawn.png").convert_alpha(), (size, size))
black_queen = pygame.transform.scale(pygame.image.load("b_queen.png").convert_alpha(), (size, size))
black_rook = pygame.transform.scale(pygame.image.load("b_rook.png").convert_alpha(), (size, size))
white_bishop = pygame.transform.scale(pygame.image.load("w_bishop.png").convert_alpha(), (size, size))
white_king = pygame.transform.scale(pygame.image.load("w_king.png").convert_alpha(), (size, size))
white_knight = pygame.transform.scale(pygame.image.load("w_knight.png").convert_alpha(), (size, size))
white_pawn = pygame.transform.scale(pygame.image.load("w_pawn.png").convert_alpha(), (size, size))
white_queen = pygame.transform.scale(pygame.image.load("w_queen.png").convert_alpha(), (size, size))
white_rook = pygame.transform.scale(pygame.image.load("w_rook.png").convert_alpha(), (size, size))


# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()


pygame.quit()
