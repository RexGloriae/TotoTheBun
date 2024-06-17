# import needed libraries
import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

# init pygame and set title
pygame.init()
pygame.display.set_caption("Toto the Bun: the Great Carrot Adventure")

# screen dimensions
WIDTH, HEIGHT = 1000, 800

# in-game frames per second
FPS = 60

# speed at which the player moves on screen
PLAYER_SPEED = 5

# game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# background function
def getBackground(level):
    if level > 8:
        level = level%8 + 1
    if level == 1:
        img = pygame.image.load("assets/Backgrounds/m1/PRE_ORIG_SIZE.png")
    elif level == 2:
        img = pygame.image.load("assets/Backgrounds/m2/PRE_ORIG_SIZE.png")
    elif level == 3:
        img = pygame.image.load("assets/Backgrounds/m3/PRE_ORIG_SIZE.png")
    elif level == 4:
        img = pygame.image.load("assets/Backgrounds/m4/PRE_ORIG_SIZE.png")
    elif level == 5:
        img = pygame.image.load("assets/Backgrounds/m5/PRE_ORIG_SIZE.png")
    elif level == 6:
        img = pygame.image.load("assets/Backgrounds/m6/PRE_ORIG_SIZE.png")
    elif level == 7:
        img = pygame.image.load("assets/Backgrounds/m7/PRE_ORIG_SIZE.png")
    elif level == 8:
        img = pygame.image.load("assets/Backgrounds/m8/PRE_ORIG_SIZE.png")
    return img

# main function
def main(screen):
    clock = pygame.time.Clock()
    
    # game run loop
    run = True
    while run:
        clock.tick(FPS)  
        
        # manage Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit if players closes screen
                run = False
                break
        
        # set BackGround    
        background_img = getBackground(1)
        background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
        screen.blit(background_img, (0, 0))
        pygame.display.flip()
            
    pygame.quit()
    quit()

# works only if ran from main file
if __name__ == "__main__":
    main(screen)
    