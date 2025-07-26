# import needed libraries and modules
import pygame

from loaders import loadEnemySprites

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    LATENCY = 3
    
    def __init__(self, x, y, width, height, dx, name = "None"):
        super().__init__()
        
        self.SPRITES = loadEnemySprites(width, height, name)
        
        self.rect = pygame.Rect(x, y, width, height)
        
        self.name = name
        
        self.mask = None
        
        self.direction = "right"
        self.animation_count = 0
        self.speed = 3
        self.movement_range = dx
        self.distance_covered = 0
        
        self.hit = False
        self.hit_count = 0
        self.invincibility = False
        
        self.attacks = False
        self.attack_count = 0
        
        
        self.lives = True
        
        
    def move(self, dx):
        self.rect.x += dx
        
    def getHit(self):
        self.hit = True
        self.hit_count = 0
        
    def moveLeft(self, speed):
        self.speed = -speed
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
            
    def moveRight(self, speed):
        self.speed = speed
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        if self.hit == False and self.attacks == False:
            self.move(self.speed)

            self.distance_covered += abs(self.speed)

            if self.distance_covered >= self.movement_range:
                self.speed = -self.speed
                self.distance_covered = 0
                if self.direction == "left":
                    self.direction = "right"
                else:
                    self.direction = "left"
        
        if self.hit:
            self.hit_count += 1
        
        if self.hit_count > fps // 2:
            self.hit = False
            self.hit_count = 0
            self.invincibility = False
            if self.health <= 0:
                self.lives = False
                
        if self.attacks:
            self.attack_count += 1
            
        if self.attack_count > fps // 2:
            self.attacks = False
            self.attack_count = 0
            if self.speed > 0:
                self.direction = "right"
            else:
                self.direction = "left"
            
        self.updateSprite()
        
    def updateSprite(self):
        sprite_sheet = "move"
        if self.health <= 0:
            sprite_sheet = "death"
            self.invincibility = True
        elif self.hit:
            sprite_sheet = "hurt"
        elif self.attacks:
            sprite_sheet = "attack"
            
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        
        if sprite_sheet == "death":
            index = (self.animation_count // 10) % len(sprites)
        else:
            index = (self.animation_count // self.LATENCY) % len(sprites)
        
        self.sprite = sprites[index]
        self.animation_count += 1
        
        self.update()
        
    def update(self):
        self.rect = self.sprite.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        
    def draw(self, disp, dx, dy):
        disp.blit(self.sprite, (self.rect.x - dx, self.rect.y - dy))
            
# slime enemy
class Slime(Enemy):
    def __init__(self, x, y, width, height, dx):
        super().__init__(x, y, width, height, dx, "slime")
        
        self.health = 1
        self.points = 2
        
        self.distance = dx
        


class Demon(Enemy):
    def __init__(self, x, y, width, height, dx):
        super().__init__(x, y, width, height, dx, "demon")
        
        self.health = 3
        self.points = 10
        
        self.distance = dx
        
