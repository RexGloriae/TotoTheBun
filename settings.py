# import libraries
import pygame

# init pygame and set title
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Toto the Bun: the Great Carrot Adventure")

# screen dimensions
WIDTH, HEIGHT = 1000, 800

# in-game frames per second
FPS = 60

# speed at which the player moves on screen
PLAYER_SPEED = 7

# game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))