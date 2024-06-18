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
PLAYER_SPEED = 6

# game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def flipImg(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def loadTrapSheet(width, height):
    all_sprites = {}
    
    # load Fire Sprites
    fire_sprites = []
    
    # load spike
    spike = pygame.image.load(f'assets/Traps/Spike/Idle.png').convert_alpha()
    scale = height 

def loadSpriteSheet(player_width, player_height):
    
    all_sprites = {}
    
    # Load Running Sprites
    running_sprites = []
    for i in range(1, 5):
        running_sprite = pygame.image.load(f'assets/Player_Sprites/Running/a{i}.png').convert_alpha()
        scale = player_height / running_sprite.get_height()
        new_width = running_sprite.get_width() * scale
        new_height = running_sprite.get_height() * scale
        running_sprite = pygame.transform.scale(running_sprite, (new_width, new_height))
        running_sprites.append(running_sprite)
    
    all_sprites["run" + "_right"] = running_sprites
    all_sprites["run" + "_left"] = flipImg(running_sprites)
        
    # Load Jumping Sprites
    jumping_sprites = []
    
    sprite = pygame.image.load(f'assets/Player_Sprites/Jump/a2.png').convert_alpha()
    scale = player_height / sprite.get_height()
    new_width = sprite.get_width() * scale
    new_height = sprite.get_height() * scale
    sprite = pygame.transform.scale(sprite, (new_width, new_height))
    jumping_sprites.append(sprite)
    
    all_sprites["jump" + "_right"] = jumping_sprites
    all_sprites["jump" + "_left"] = flipImg(jumping_sprites)
    
    # Load Fall Sprites
    falling_sprites = []
    
    sprite = pygame.image.load(f'assets/Player_Sprites/Jump/a5.png').convert_alpha()
    scale = player_height / sprite.get_height()
    new_width = sprite.get_width() * scale
    new_height = sprite.get_height() * scale
    sprite = pygame.transform.scale(sprite, (new_width, new_height))
    falling_sprites.append(sprite)
    
    all_sprites["fall" + "_right"] = falling_sprites
    all_sprites["fall" + "_left"] = flipImg(falling_sprites)
            
    # Load Faint Sprite
    faint_sprites = []
    for i in range(1, 6):
        sprite = pygame.image.load(f'assets/Player_Sprites/Faint/a{i}.png').convert_alpha()
        scale = player_height / sprite.get_height()
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        faint_sprites.append(sprite)
        
    all_sprites["faint" + "_right"] = faint_sprites
    all_sprites["faint" + "_left"] = flipImg(faint_sprites)
        
    # Load Dizzy Sprite
    dizzy_sprites = []
    for i in range(1, 3):
        sprite = pygame.image.load(f'assets/Player_Sprites/Dizzy/a{i}.png').convert_alpha()
        scale = player_height / sprite.get_height()
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        dizzy_sprites.append(sprite)
        
    all_sprites["dizzy" + "_right"] = dizzy_sprites
    all_sprites["dizzy" + "_left"] = flipImg(dizzy_sprites)
        
    # Load Idle Sprite
    idle_sprites = []
    for i in range(1, 3):
        sprite = pygame.image.load(f'assets/Player_Sprites/Idle/a{i}.png').convert_alpha()
        scale = player_height / sprite.get_height()
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        idle_sprites.append(sprite)
        
    all_sprites["idle" + "_right"] = idle_sprites
    all_sprites["idle" + "_left"] = flipImg(idle_sprites)
    
    # load Shoot Sprite
    shoot_sprites = []
    for i in range(1, 4):
        sprite = pygame.image.load(f'assets/Player_Sprites/Shoot/a{i}.png').convert_alpha()
        scale = player_height / sprite.get_height()
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        shoot_sprites.append(sprite)
    
    all_sprites["shoot" + "_right"] = shoot_sprites
    all_sprites["shoot" + "_left"] = flipImg(shoot_sprites)
    
    # load Health Sprite
    health_sprites = []
    for i in range(1, 9):
        sprite = pygame.image.load(f'assets/Player_Sprites/HearTile/Cuore{i}.png').convert_alpha()
        scale = player_height / sprite.get_height() // 2
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        health_sprites.append(sprite)
    
    all_sprites["health"] = health_sprites
    
    return all_sprites


# load terrain
def loadBlock(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    
    return pygame.transform.scale2x(surface)

# Player Class
class Player(pygame.sprite.Sprite):
    COLOR=(255, 0, 0)
    GRAVITY = 1
    
    SPRITES = loadSpriteSheet(64, 64)
    LATENCY = 3
    
    def __init__(self, x, y, width, height):
        super().__init__()
        
        self.rect = pygame.Rect(x, y, width, height)
        
        self.x_speed = 0
        self.y_speed = 0
        
        self.mask = None
        
        self.direction = "left"
        self.animation_count = 0
        
        self.fall_count = 0
        self.jump_count = 0
        
    def jump(self):
        multiplier = 6
        if self.jump_count == 1:
            multiplier = 9
        
        self.y_speed = -self.GRAVITY * multiplier
        self.animation_count = 0
        self.jump_count += 1
        
        if self.jump_count == 1:
            self.fall_count = 0
        
        
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
    def moveLeft(self, speed):
        self.x_speed = -speed
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
        
    def moveRight(self, speed):
        self.x_speed = speed
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    
    def loop(self, fps):
        self.y_speed += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_speed, self.y_speed)
        
        self.fall_count += 1
        
        self.updateSprite()
        
    def landed(self):
        self.fall_count = 0
        self.y_speed = 0
        self.jump_count = 0
        
    def hitHead(self):
        self.count = 0
        self.y_speed *= -1
        
        
    def updateSprite(self):
        sprite_sheet = "idle"
        if self.y_speed < 0:
            sprite_sheet = "jump"
        elif self.y_speed > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_speed != 0:
            sprite_sheet = "run"
            
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        
        index = (self.animation_count // self.LATENCY) % len(sprites)
        
        self.sprite = sprites[index]
        self.animation_count += 1
        
        self.update()
        
    def update(self):
        self.rect = self.sprite.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        
        
    def draw(self, disp, offset_x):
        disp.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name = None):
        super().__init__()
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
        
    def draw(self, disp, offset_x):
        disp.blit(self.image, (self.rect.x - offset_x, self.rect.y))
        
        
class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        
        block = loadBlock(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Fire(Object):
    def __init__(self, x, y, width, height):
        super().__init__(self, x, y, width, height, "fire")
        self.fire 
        

def handleVerticalCollision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hitHead()
        collided_objects.append(obj)
        
    return collided_objects

def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    
    collided_object = None
    
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break
        
    player.move(-dx, 0)
    player.update()
    
    return collided_object

def handleMovement(player, objects):
    keys = pygame.key.get_pressed()
    
    collide_left = collide(player, objects, -PLAYER_SPEED * 2)
    collide_right = collide(player, objects, PLAYER_SPEED * 2)
    
    
    player.x_speed = 0
    if keys[pygame.K_a] and not collide_left:
        player.moveLeft(PLAYER_SPEED)
    if keys[pygame.K_d] and not collide_right:
        player.moveRight(PLAYER_SPEED)
        
    handleVerticalCollision(player, objects, player.y_speed)

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

def drawScreen(screen, level, player, objects, offset_x):
    # set BackGround    
    background_img = getBackground(1)
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
    screen.blit(background_img, (0, 0))
    
    # draw objects
    for obj in objects:
        obj.draw(screen, offset_x)
    
    # draw Player
    player.draw(screen, offset_x)
    
    pygame.display.update()    

# main function
def main(screen):
    clock = pygame.time.Clock()
    
    
    # generate Player
    player = Player(100, 100, 50, 50)
    
    # generate blocks
    block_size = 96 
    
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]
    
    objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size), Block(block_size * 3, HEIGHT - block_size * 4, block_size)]
    
    offset_x = 0
    scrolling_area_width = 200
    
    # game run loop
    run = True
    while run:
        clock.tick(FPS)  
        
        # manage Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit if players closes screen
                run = False
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and player.jump_count < 2:
                    player.jump()
                    
        player.loop(FPS)
        handleMovement(player, objects)
        drawScreen(screen, 1, player, objects, offset_x)
        
        if ((player.rect.right - offset_x >= WIDTH - scrolling_area_width) and player.x_speed > 0) or (
            (player.rect.left - offset_x <= scrolling_area_width) and player.x_speed < 0):
            offset_x += player.x_speed
            
    pygame.quit()
    quit()

# works only if ran from main file
if __name__ == "__main__":
    main(screen)
    