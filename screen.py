# import libraries and modules
import pygame
import settings

from loaders import getBackground

def drawText(screen, text, size, color, x, y):
    font = pygame.font.Font("assets/Fonts/pcsenior.ttf", size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def drawScreen(screen, level, player, objects, collectibles, enemies, offset_x, offset_y):
    # set BackGround    
    background_img = getBackground(level)
    background_img = pygame.transform.scale(background_img, (settings.WIDTH, settings.HEIGHT))
    screen.blit(background_img, (0, 0))
    
    # draw objects
    for obj in objects:
        obj.draw(screen, offset_x, offset_y)
        
    # draw collectibles
    for obj in collectibles:
        if obj.touched == 0:
            obj.draw(screen, offset_x, offset_y)
    
    # draw Player
    player.draw(screen, offset_x, offset_y)
    
    # draw enemies
    for entity in enemies:
        if entity.lives:
            entity.draw(screen, offset_x, offset_y)
    
    # draw Score
    drawText(screen, f"Score = {player.score}", 16, (0, 0, 0), settings.WIDTH - 180, 8)
    
    # draw game over text
    if player.health == 0:
        drawText(screen, "Game Over!", 64, (0, 0, 0), settings.WIDTH // 5, settings.HEIGHT / 2.5)
        
    # draw level finished text
    if player.will_teleport:
        drawText(screen, "Level Finished!", 64, (0, 0, 0), 30, settings.HEIGHT / 2.5)
    
    pygame.display.update() 