# import needed libraries
import pygame

def flipImg(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]