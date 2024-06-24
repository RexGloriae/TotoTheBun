# import needed libraries and modules
import pygame

from loaders import loadSpriteSheet, loadHealthSprites
from settings import screen

# Player Class
class Player(pygame.sprite.Sprite):
    COLOR=(255, 0, 0)
    GRAVITY = 1
    
    SPRITES = loadSpriteSheet(64, 64)
    LATENCY = 3
    
    HEALTH_IMG = loadHealthSprites(30, 30)
    
    def __init__(self, x, y, width, height, restart_game_callback):
        super().__init__()
        
        self.restart_game_callback = restart_game_callback
        
        self.rect = pygame.Rect(x, y, width, height)
        
        self.x_speed = 0
        self.y_speed = 0
        
        self.mask = None
        
        self.direction = "right"
        self.animation_count = 0
        
        self.fall_count = 0
        self.jump_count = 0
        
        self.hit = False
        self.hit_count = 0
        
        self.health = 3
        self.invincibility = False
        self.health_anim = 0
        
        self.score = 0
        
        self.will_teleport = False
        self.teleport_count = 0
        
    def jump(self):
        multiplier = 7
        if self.jump_count == 1:
            multiplier = 10
        
        self.y_speed = -self.GRAVITY * multiplier
        self.animation_count = 0
        self.jump_count += 1
        
        if self.jump_count == 1:
            self.fall_count = 0
        
        
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
    def getHit(self):
        self.hit = True
        self.hit_count = 0
        
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
        
        if self.hit:
            self.hit_count += 1
            
        if self.hit_count > fps // 2:
            self.hit = False
            self.hit_count = 0
            self.invincibility = False
            if self.health <= 0:
                self.restart_game_callback(screen)
                
        if self.will_teleport:
            self.teleport_count += 1
            
        if self.teleport_count > fps // 2:
            self.restart_game_callback(screen)
        
        self.fall_count += 1
        
        self.updateSprite()
        
    def landed(self):
        self.fall_count = 0
        self.y_speed = 0
        self.jump_count = 0
        
    def hitHead(self):
        self.count = 0
        self.y_speed *= -1
    
    def displayHealth(self, disp):
        index = (self.health_anim // self.LATENCY) % len(self.HEALTH_IMG)
        for life in range(self.health):
            sprite = self.HEALTH_IMG[index]
            x_pos = 10 + life * (sprite.get_width() + 10)
            y_pos = 10
            disp.blit(sprite, (x_pos, y_pos))
        
    def updateSprite(self):
        sprite_sheet = "idle"
        if self.health <= 0:
            sprite_sheet = "faint"
            self.invincibility = True
        elif self.will_teleport:
            sprite_sheet = "explode"
        elif self.hit:
            sprite_sheet = "dizzy"
        elif self.y_speed < 0:
            sprite_sheet = "jump"
        elif self.y_speed > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_speed != 0:
            sprite_sheet = "run"
            
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        
        if sprite_sheet == "faint":
            index = (self.animation_count // 10) % len(sprites) # value for which the animation works (if it works, don't change it)
        elif sprite_sheet == "explode":
            index = (self.animation_count // 5) % len(sprites) # value for which the animation works (if it works, don't change it)
        else:
            index = (self.animation_count // self.LATENCY) % len(sprites)
        
        self.sprite = sprites[index]
        self.animation_count += 1
        
        self.health_anim += 1
        if(self.health_anim >= len(self.HEALTH_IMG) * self.LATENCY):
            self.health_anim = 0
            
        
        self.update()
        
    def update(self):
        self.rect = self.sprite.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        
        
    def draw(self, disp, offset_x, offset_y):
        disp.blit(self.sprite, (self.rect.x - offset_x, self.rect.y - offset_y))
        self.displayHealth(disp)
