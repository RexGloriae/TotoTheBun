# import needed libraries and modules
import os
import random
import math
import pygame

from settings import WIDTH, HEIGHT, PLAYER_SPEED, screen, FPS
from menu import mainMenu
from levels import getLevelMusic, loadLevel
from player_class import Player
from loaders import loadSoundEffects
from screen import drawScreen, drawText
from events import handleMovement, handleEnemies, handleCollectibles



def loopTraps(traps):
    for obj in traps:
        obj.loop()
        
def loopCollectibles(items):
    for obj in items:
        obj.loop()
        
def loopEnemies(enemies, fps):
    for enemy in enemies:
        enemy.loop(fps)


# main function
def main(screen):
    level = None
    
    pygame.mixer.stop()
    music = pygame.mixer.Sound("assets/Sounds/Music/menu.wav")
    music.play(-1)
    music.set_volume(0.5)
    
    while not level:
        level = mainMenu(screen, WIDTH, HEIGHT)

    music.stop()
    
    music = getLevelMusic(level)
    music.play(-1)
    music.set_volume(0.5)
        
    clock = pygame.time.Clock()
        
    # generate Player
    player = Player(100, HEIGHT - 96 - 50, 50, 50, main)
    
    # load level map
    block_size = 96 
    
    objects, traps, collectibles, enemies = loadLevel(level)
    
    # load sounds
    sounds = loadSoundEffects()
    
    # background scrolling variables
    offset_x = 0
    scrolling_area_width = 200
    
    offset_y = 0
    top_height = 300
    bottom_height = 300
    scrolling_height = HEIGHT
    
    # check if game is paused
    IS_PAUSED = False
    # game run loop
    run = True
    while run:
        # manage Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit if players closes screen
                run = False
                break
            
            
            # manage game pausing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    IS_PAUSED = not IS_PAUSED
                    if IS_PAUSED:
                        drawText(screen, "Game Paused!", 64, (0, 0, 0), WIDTH // 7, HEIGHT / 2.5)
                        pygame.display.flip()
                elif event.key == pygame.K_ESCAPE:
                    main(screen)
                
                if not IS_PAUSED and player.health > 0:
                    if event.key == pygame.K_w and player.jump_count < 2:
                        player.jump()
        if not IS_PAUSED:

            player.loop(FPS)
            loopTraps(traps)
            loopCollectibles(collectibles)
            loopEnemies(enemies, FPS)
            handleMovement(player, objects, sounds)
            handleEnemies(player, enemies, sounds)
            handleCollectibles(player, collectibles, sounds)
            drawScreen(screen, level, player, objects, collectibles, enemies, offset_x, offset_y)

            if ((player.rect.right - offset_x >= WIDTH - scrolling_area_width) and player.x_speed > 0) or (
                (player.rect.left - offset_x <= scrolling_area_width) and player.x_speed < 0):
                offset_x += player.x_speed
            
                
            if scrolling_height > HEIGHT:
                if ((player.rect.top - offset_y <= scrolling_height - 300) and player.y_speed < 0) or (
                    (player.rect.bottom - offset_y >= scrolling_height - (abs(offset_y) + 2 * block_size)) and player.y_speed > 0.5):
                    offset_y += player.y_speed
                scrolling_height = HEIGHT - offset_y
            else:
                if ((player.rect.top - offset_y >= scrolling_height + 300) and player.y_speed < 0) or (
                    (player.rect.bottom - offset_y <= scrolling_height + (abs(offset_y) + 2 * block_size)) and player.y_speed > 0.5):
                    offset_y += player.y_speed
                scrolling_height = HEIGHT + offset_y

    pygame.quit()
    quit()

# works only if ran from main file
if __name__ == "__main__":
    main(screen)
    